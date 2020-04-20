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
    serializer_class = MenuSerializer
    pagination_class = SmallPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','store','menu_name', 'price']
    queryset = Menu.objects.all()

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
from .openapis import *
import mysql.connector as mariadb
# 거리 : 반경 x km 이내 (현재 위치든 다른 곳이든 위치를 받아야함)
# 맛   : 각 가게의 리뷰점수를 평균내서 순위매긴 값이 유저가 원하는 최소 평점 수치 y보다 높아아야함
# 가격 : 각 가게들의 메뉴 평균인데, 메뉴가 없는가게도 많아서 0원 처리되는 곳이 꽤 많음
# 거르는 음식 : 메뉴 이름정도로 거르던지 해야하는 상태... -> 이걸로 가게를 거르긴 좀..그래서 없음
# 후에 웨이팅 시간이 추가된다면 더 넣도록
'''
headers = {'Content-Type': 'application/json; charset=utf-8', "mimetype" : "applications/json"}
data = {
        "searchOptions": {
            "orderby": "avg_score",
            "searchType": "user",
            "searchNum": "one"
        },
        "userInfo": [
            {
                "curLatitude": "37.503652",
                "curLongitude": "127.038125"
            },
            {
                "curLatitude": "38.503652",
                "curLongitude": "127.038125"
            }
        ],
        "areaInfo": [],
        "maxDistance": "0.3",
        "minPoint": "3",
        "maxPrice": "20000",
        "foodfilter": ""
    }
'''
# 개인/모임 유저, 지역/여러지역 합산 버전 
@api_view(['POST'])
def searchRealPrice(request):
    if request.method =='POST':
        data = request.data
        # geoResponse = geoCoding("강남구 역삼동")
        # # print(geoResponse.status_code)
        # geoData = geoResponse.json()
        # print(geoData)
        # print(geoData["meta"])
        # print(geoData["addresses"][0]["x"])
        # print(geoData["addresses"][0]["y"])
        # print(geoResponse.addresses.y)
        # response = reverseGeoCoding("127.038125","37.503652")
        # test = {}
        # test["header"] = json.dumps(dict(response.headers))
        # test["encoding"] = response.encoding
        # test["status_code"] = response.status_code
        # test["data"] = response.json()

        # print(json.dumps(test, indent=2, separators=(',', ': '), ensure_ascii = False))
        ## preprocess searchOptions
        # orderby = "distance" if(data["searchOptions"]["orderby"] == "") else (data["searchOptions"]["orderby"])
        # if (orderby == "avg_score"):
        #     orderby += " desc"
        # searchType = "user" if(data["searchOptions"]["searchType"] == "" or data["searchOptions"]["searchType"] == "user") else "area"
        # searchNum = "one" if(data["searchOptions"]["searchNum"] == "" or data["searchOptions"]["searchNum"] == "one") else "many"
        # userList = data["userInfo"]
        # curLatitude = 0
        # curLongitude = 0
        # if searchNum == "many":
        #     for user in userList:
        #         curLatitude += user["curLatitude"]
        #         curLongitude += user["curLongitude"]
        # print(curLatitude, curLongitude)
    #     # 여기서 숫자가 1명이면 그대로 진행하면 되고 1지역이면 네이버api를 이용해서 curLatitude, curLongitude 변경해줘야함
    #     # 여기서 숫자가 여러명이면 평균값 구하기. 일부 사람 수 제외 시는 프론트에서 제어해주는게 좋을듯
    #     #              여러지역이면 각 지역별로 네이버 api 이용해서 구한 뒤, 평균값인데
    #     # 실제로 사용자가 이용한다고 했을때,
    #     #        다른 유저들의 위치정보를 상세하게는 알 수 없을 것인데, 네이버api가 가능해지면 전부다 주소로 입력받아서 할지
    #     #        각자 자신 위치를 설정할 수 있게 할 것인지. 미리 각자 주소를 등록해두게 할 것인지 결정해야함
    #     # 따라서 일단 네이버api로 주소를 좌표값으로 바꾸는 geocoding 하도록 할 것
    #     curLatitude = str(data["curLatitude"])
    #     curLongitude = str(data["curLongitude"])
    #     maxDistance = str(data["maxDistance"])
    #     minPoint = str(data["minPoint"])
    #     maxPrice = str(data["maxPrice"])


    #     sql = "SELECT s.*, ROUND(AVG(m.price),0) AS avg_price\
    #             FROM\
    #                 (SELECT\
    #                 s.*,\
    #                 AVG(r.score) AS avg_score,\
    #                 COUNT(r.id) AS cnt_review,\
    #                 round((6371\
    #                     *acos(\
    #                     (cos(radians("+curLatitude+"))*cos(radians(s.latitude))*cos(radians(s.longitude)-radians("+curLongitude+")))+\
    #                     (sin(radians("+curLatitude+"))*sin(radians(s.latitude)))\
    #                     )\
    #                 ),3) AS distance\
    #                 FROM api_store AS s\
    #                 JOIN api_review AS r\
    #                 ON s.id = r.store\
    #                 GROUP BY s.id\
    #                 HAVING distance < "+maxDistance+" AND avg_score > "+minPoint+") s\
    #             JOIN api_menu m\
    #             ON s.id = m.store\
    #             GROUP BY m.store\
    #             HAVING avg_price <= "+maxPrice +" order by "+orderby+";"
        
    #     # access db, excute sql and fetch data 
    #     mariadbConnection = mariadb.connect(user='root', password='ssafy', database='realpricedb', host="13.125.68.33")
    #     cursor = mariadbConnection.cursor()
    #     cursor.execute(sql)
    #     columns = [col[0] for col in cursor.description]
    #     merged_data =[
    #         dict(zip(columns, row))
    #         for row in cursor.fetchall()
    #     ]
    #     mariadbConnection.close()      
    
    # response = {
    #     'count':len(merged_data),
    #     'result':merged_data,
    # }
    # response['message']='검색된 맛집 추천 리스트입니다.' if response['count'] > 0 else '검색된 결과가 없습니다'
    # return Response({'received_data':response})
    return Response({'received_data':request.data})

# 개인유저 버전
# @api_view(['POST'])
# def searchRealPrice(request):
#     data = request.data
#     orderby = "distance" if(data["orderby"] == "") else data["orderby"]
#     if orderby == "avg_score":
#         orderby += " desc"
#     if request.method =='POST':
#         curLatitude = str(data["curLatitude"])
#         curLongitude = str(data["curLongitude"])
#         maxDistance = str(data["maxDistance"])
#         minPoint = str(data["minPoint"])
#         maxPrice = str(data["maxPrice"])
#         sql = "SELECT s.*, ROUND(AVG(m.price),0) AS avg_price\
#                 FROM\
#                     (SELECT\
#                     s.*,\
#                     AVG(r.score) AS avg_score,\
#                     COUNT(r.id) AS cnt_review,\
#                     round((6371\
#                         *acos(\
#                         (cos(radians("+curLatitude+"))*cos(radians(s.latitude))*cos(radians(s.longitude)-radians("+curLongitude+")))+\
#                         (sin(radians("+curLatitude+"))*sin(radians(s.latitude)))\
#                         )\
#                     ),3) AS distance\
#                     FROM api_store AS s\
#                     JOIN api_review AS r\
#                     ON s.id = r.store\
#                     GROUP BY s.id\
#                     HAVING distance < "+maxDistance+" AND avg_score > "+minPoint+") s\
#                 JOIN api_menu m\
#                 ON s.id = m.store\
#                 GROUP BY m.store\
#                 HAVING avg_price <= "+maxPrice +" order by "+orderby+";"
#         mariadb_connection = mariadb.connect(user='root', password='ssafy', database='realpricedb', host="13.125.68.33")
#         cursor = mariadb_connection.cursor()
#         cursor.execute(sql)
#         # fetchall = cursor.fetchall()
#         columns = [col[0] for col in cursor.description]
#         merged_data =[
#             dict(zip(columns, row))
#             for row in cursor.fetchall()
#         ]
#         mariadb_connection.close()       
#     response = {
#         'count':len(merged_data),
#         'result':merged_data,
#     }
#     response['message']='검색된 맛집 추천 리스트입니다.' if response['count'] > 0 else '검색된 결과가 없습니다'
#     return Response({'received_data':response})
    




