from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from .models import User

class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50

from rest_framework import filters
class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    pagination_class = SmallPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['store_name', 'area']
    def get_queryset(self):
        name = self.request.query_params.get("name", "")
        queryset = (
            Store.objects.all().filter(store_name__contains=name).order_by("id")
        )
        return queryset


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    pagination_class = SmallPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['faq_title']

    queryset = Faq.objects.all()

class QnaViewSet(viewsets.ModelViewSet):
    serializer_class = QnaSerializer
    pagination_class = SmallPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['qna_title']

    queryset = Qna.objects.all()
    # queryset filtering depth 1이고 title이 name인 애만 

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = SmallPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']
    
    queryset = User.objects.all()

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = SmallPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','store','user', 'score']
    queryset = Review.objects.all()

class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    pagination_class = SmallPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['history_no']
    queryset = History.objects.all()

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = SmallPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','store','menu_name', 'price']
    queryset = Review.objects.all()

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

'''
data format 요청할때 이렇게 넣을 것
{
	"curLatitude": "37.503652",
	"curLongitude": "127.038125",
	"maxDistance": "0.3",
	"minPoint": "3",
	"maxPrice": "20000",
	"foodfilter": "",
   	"orderby": "avg_score" 
} #orderby는 "distance"(오름차순), "avg_score"(내림차순), "avg_price"(오름차순)입니다.
'''

import mysql.connector as mariadb

@api_view(['GET'])
def checkUsedEmail(request, email):
    response = {}
    if request.method == 'GET':
        try:
            queryset = User.objects.get(email=email)
            response["message"] = "User Email is Duplicated."
            response["status"] = status.HTTP_200_OK
        except User.DoesNotExist:  
            response["message"] = "User Email isn't Duplicated. You can use this email ["+str(email)+"]"
            response["status"] = status.HTTP_204_NO_CONTENT
    return Response(response)

@api_view(['PUT'])
def follow(request, user_id):
    people = get_object_or_404(get_user_model(), id=user_id)
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else :
        people.followers.add(request.user)
    return redirect('api/users', request.user)


@api_view(['POST'])
def searchRealPrice(request):#, format=None):
# 거리 : 반경 x km 이내 (현재 위치든 다른 곳이든 위치를 받아야함)
# 맛   : 각 가게의 리뷰점수를 평균내서 순위매긴 값이 유저가 원하는 최소 평점 수치 y보다 높아아야함
# 가격 : 각 가게들의 메뉴 평균인데, 메뉴가 없는가게도 많아서 0원 처리되는 곳이 꽤 많음
# 거르는 음식 : 메뉴 이름정도로 거르던지 해야하는 상태... -> 이걸로 가게를 거르긴 좀..그래서 없음
# 후에 웨이팅 시간이 추가된다면 더 넣도록
    data = request.data
    orderby = "distance" if(data["orderby"] == "") else data["orderby"]
    if orderby == "avg_score":
        orderby += " desc"
    if request.method =='POST':
        curLatitude = str(data["curLatitude"])
        curLongitude = str(data["curLongitude"])
        maxDistance = str(data["maxDistance"])
        minPoint = str(data["minPoint"])
        maxPrice = str(data["maxPrice"])
        sql = "SELECT s.*, ROUND(AVG(m.price),0) AS avg_price\
                FROM\
                    (SELECT\
                    s.*,\
                    AVG(r.score) AS avg_score,\
                    COUNT(r.id) AS cnt_review,\
                    round((6371\
                        *acos(\
                        (cos(radians("+curLatitude+"))*cos(radians(s.latitude))*cos(radians(s.longitude)-radians("+curLongitude+")))+\
                        (sin(radians("+curLatitude+"))*sin(radians(s.latitude)))\
                        )\
                    ),3) AS distance\
                    FROM api_store AS s\
                    JOIN api_review AS r\
                    ON s.id = r.store\
                    GROUP BY s.id\
                    HAVING distance < "+maxDistance+" AND avg_score > "+minPoint+") s\
                JOIN api_menu m\
                ON s.id = m.store\
                GROUP BY m.store\
                HAVING avg_price <= "+maxPrice +" order by "+orderby+";"
        mariadb_connection = mariadb.connect(user='root', password='ssafy', database='realpricedb', host="13.125.68.33")
        cursor = mariadb_connection.cursor()
        cursor.execute(sql)
        # fetchall = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        merged_data =[
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        mariadb_connection.close()       
    response = {
        'count':len(merged_data),
        'result':merged_data,
    }
    response['message']='검색된 맛집 추천 리스트입니다.' if response['count'] > 0 else '검색된 결과가 없습니다'
    return Response({'received_data':response})


# 원본
# @api_view(['POST'])
# def searchRealPrice(request):#, format=None):
# # 거리 : 반경 x km 이내 (현재 위치든 다른 곳이든 위치를 받아야함)
# # 맛   : 각 가게의 리뷰점수를 평균내서 순위매긴 값이 유저가 원하는 최소 평점 수치 y보다 높아아야함
# # ---현재 여기까지
# # ---문제 전체 호출 한번해서 너무 느림 - 쿼리로 좀 축소해서 가져오고 싶은데 마음대로 못 다루겠음
# # 메뉴가 없어서 진행을 더이상 할 수가 없음!! 어쨌든 현재 할 수 있는 상태에서 효율적인 방법을 찾아보겠음
# # 가격 : 메뉴 추출해서 작업하고 있어야함...
# # 거르는 음식 : 메뉴 이름정도로 거르던지 해야하는 상태... -> 이걸로 가게를 거르긴 좀..
# # 후에 웨이팅 시간이 추가된다면 
#     storeList = Store.objects.all()
#     # 대표 메뉴의 가격 or 평균가격이 매겨지면 filtering 처리하면 좀 더 빠르긴 할 것
#     reviewList = Review.objects.values('store').annotate(
#         average = Avg('score')
#     ).values('average', 'store')
 
#     data = request.data

#     merged_data = []
#     if request.method =='POST':
#         curLatitude = float(data["curLatitude"])
#         curLongitude = float(data["curLongitude"])
#         maxDistance = float(data["maxDistance"])
#         minPoint = float(data["minPoint"])
#         for store in storeList:
#             # 반경 거리 이내에 존재
#             if maxDistance >= haversine((store.latitude,store.longitude), (curLatitude,curLongitude), unit='km'):
#                 # searching element dictionary in list (현재 본 스토어의 리뷰점수까지 )
#                 review = list(filter(lambda review: review['store'] == store.id and minPoint <= float(review['average']), reviewList))
#                 if review:
#                     result = {}
#                     result["id"] = store.id
#                     result["store_name"] = store.store_name
#                     result["branch"] = store.branch
#                     result["area"] = store.area
#                     result["address"] = store.address
#                     result["tel"] = store.tel
#                     result["category_list"] = store.category_list
#                     result["latitude"] = store.latitude
#                     result["longitude"] = store.longitude
#                     result["rating"] = review[0]['average']
#                     if result not in merged_data: 
#                         merged_data.append(result)
#     merged_data = sorted(merged_data, key=lambda data: data['rating'], reverse=True)          
#     response = {
#         'count':len(merged_data),
#         'result':merged_data,
#     }
#     response['message']='검색된 맛집 추천 리스트입니다.' if response['count'] > 0 else '검색된 결과가 없습니다'
#     return Response({'received_data':response})
#     # response = json.dumps(response)
#     # return HttpResponse(response, mimetype="application/json")
# # 사용자 위치부터 최대반경 거리
# # 최소별점
# # 최소가격, 최대가격 받고
# # 거르는 음식 기본 null값


