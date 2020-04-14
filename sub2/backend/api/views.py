from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
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
    
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from haversine import haversine
from django.db.models import Avg
import json
from django.http.response import HttpResponse

'''
data format
{
	"curLatitude": "37.503652",
	"curLongitude": "127.038125",
	"maxDistance": "0.3",
	"minPoint": "3",
	"maxPrice": "15000",
	"foodfilter": ""
}
'''
@api_view(['POST'])
def searchRealPrice(request):#, format=None):
# 거리 : 반경 x km 이내 (현재 위치든 다른 곳이든 위치를 받아야함)
# 맛   : 각 가게의 리뷰점수를 평균내서 순위매긴 값이 유저가 원하는 최소 평점 수치 y보다 높아아야함
# ---현재 여기까지
# ---문제 전체 호출 한번해서 너무 느림 - 쿼리로 좀 축소해서 가져오고 싶은데 마음대로 못 다루겠음
# ---
# 가격 : 메뉴 추출해서 작업하고 있어야함...
# 거르는 음식 : 메뉴 이름정도로 거르던지 해야하는 상태...
    storeList = Store.objects.all()
    reviewList = Review.objects.values('store').annotate(
        average = Avg('score')
    ).values('average', 'store')
 
    data = request.data

    merged_data = []
    if request.method =='POST':
        curLatitude = float(data["curLatitude"])
        curLongitude = float(data["curLongitude"])
        maxDistance = float(data["maxDistance"])
        minPoint = float(data["minPoint"])
        for store in storeList:
            # 반경 거리 이내에 존재
            if maxDistance >= haversine((store.latitude,store.longitude), (curLatitude,curLongitude), unit='km'):
                # searching element dictionary in list (현재 본 스토어의 리뷰점수까지 )
                review = list(filter(lambda review: review['store'] == store.id and minPoint <= float(review['average']), reviewList))
                if review:
                    result = {}
                    result["id"] = store.id
                    result["store_name"] = store.store_name
                    result["branch"] = store.branch
                    result["category_list"] = store.category_list
                    result["rating"] = review[0]['average']
                    if result not in merged_data: 
                        merged_data.append(result)
    merged_data = sorted(merged_data, key=lambda data: data['rating'], reverse=True)          
    response = {
        'count':len(merged_data),
        'result':merged_data,
    }
    response['message']='검색된 맛집 추천 리스트입니다.' if response['count'] > 0 else '검색된 결과가 없습니다'
    return Response({'received data':response})
    # response = json.dumps(response)
    # return HttpResponse(response, mimetype="application/json")
# 사용자 위치부터 최대반경 거리
# 최소별점
# 최소가격, 최대가격 받고
# 거르는 음식 기본 null값

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
