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
    # search_fileds를 store만 남겨두고 했는데 ?search=15 -> store에 15만 들어가면 나왔음. 15, 150 ,,,
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


@api_view(['GET'])
def getStores(request):
    data = {
        "stores": [{
                "id":1,
                "srcUrl": "https://lh3.googleusercontent.com/proxy/-oyyAgFrUNxAafWB9DU0UhQOaSsj5xK9-3_RlCAyNrChORri7y7HWNPysCRqA8yLcSbWFgzvgqgF7pR60yZZTvcr5xMImbo_4Zr2b1LnHbGmEzlh1h0t6mLwssBr9vQoQELpi-nnzS-IZEpgUcdrnKUHLtYVL_C-Z4pMNmIFO4bsXO7gCFiqvZMTby61exbtq0CNUDqjRofJim0fMsO-Bm4mt6poD4_dM-3dTH87myNa8BtjWQPgxS6fVGDodCZ1in2zjKZIWiC6cEgl1KmTEpHLiVg",
                "storeName": "이오카츠",
                "price": "12000"
            },
            {
                "id":2,
                "srcUrl": "https://lh3.googleusercontent.com/proxy/jS4i5cCRSEEU74hs1nExlt22sBl4pikpf8dhc8rjoLWwwZNbzpsHWCdQCYKTzddIbwWJH1P7eu0WJ94hHe9WwdqrQwCzy3sOd12t9aS-EPoqV2cwg_T19EO8s011dj4R-F5Sxna0ML6UkOqEvSKVDpFhr9cLxKoGmdb7OT1mCM0g1hFVKY2pR97xAIpPk7uRYXPxNKlhm9e-ah_uP3doNTr16lg15FhchLtwH5RIRo0Egv1hjIqdX67sz6B5jqjvvC8QnnFV_pyQWr62LwfgKvL6RL76BgxTlL-dDyffSR-CIfjScxHkRHlQFiVFmH1JJtsZ5srFT8LJSwj38b1JNChLOQMeAQkzbSTz6QyEKXngMc8bFx5ahommRJhI06limBLQxe23OR4kyFxicMF8JV0",
                "storeName": "강남 돈까스",
                "price": "19870"
            },
            {
                "id":3,
                "srcUrl": "https://t1.daumcdn.net/liveboard/dispatch/6301b06e0bf04496aa2b5d3a980d551c.JPG",
                "storeName": "가나돈까스의 집",
                "price": "8000"
            },
            {
                "id":4,
                "srcUrl": "https://lh3.googleusercontent.com/proxy/B-sE-Sggpv8A1cP9yLsA1tp9deiJS0z91a-NPiggDZlfGikJQfNgmtlt65W2Fvlr_y1BU6nndBbhiOKC9iot-b_ebZFRvrk6_apUOBqO0QwMmXKOlU4Cldq9rvIvsraMTmnPgn3VaaGOIHuruPldp2Ha_qXHpf3Pk5eFriGwXwhbCYt6FgHEzNVcOug",
                "storeName": "미나미야마",
                "price": "21080"
            },
            {
                "id":5,
                "srcUrl": "https://i.pinimg.com/originals/51/6f/51/516f51f23c31837500e6518cd2e00b52.jpg",
                "storeName": "한성돈까스",
                "price": "9500"
            }]
    }
    return Response(data)

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

from .openapis import *
import mysql.connector as mariadb

@api_view(['GET'])
def detailStore(request, id):
    response = {}
    message = ""
    # 중간에 foreign key를 업데이트 하는게 쉽지않은듯,, 어차피 1개짜리에 대한 정보니까 그냥 직접뽑아서 한번에 합치는게 나은듯
    # access db, excute sql and fetch data 
    sql = "SELECT * FROM api_store WHERE id = "+id+";"
    mariadbConnection = mariadb.connect(user='root', password='ssafy', database='realpricedb', host="13.125.68.33")
    cursor = mariadbConnection.cursor()
    sql = "SELECT * FROM api_store WHERE id = "+id+";"
    cursor.execute(sql)
    columns = [col[0] for col in cursor.description]
    store =[
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    if(len(store) > 0):
        message = store[0]["store_name"]+"에 관련된 정보입니다."
        sql = "SELECT * FROM api_menu WHERE store = "+id+";"
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        menus =[
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        
        sql = "SELECT * FROM api_review WHERE store = "+id+";"
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        reviews =[
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        
    else:
        message ="검색된 결과가 없습니다."
        menus = []
        reviews =[]
    mariadbConnection.close()

    response = {
        'message':message,
        'store':store,
        'menuCnt':len(menus),
        'menu':menus,
        'reviewCnt':len(reviews),
        'review': reviews
    }   
    return Response({'received_data':response})

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

'''
headers = {'Content-Type': 'application/json; charset=utf-8', "mimetype" : "applications/json"}
{
    "searchOptions": {
        "orderby": "distance", - 거리순 "distance"(오름차순), 평점 순 "avg_score"(내림차순), 가격 순 "avg_price"(오름차순)
        "searchType": "area", - 유저들의 위치를 받는다면 "user" , 지역검색을 이옹한다면 "area"
        "searchNum": "many" - 여러명 또는 여러 곳이면 "many", 한 명 또는 한 곳이면 "one"
    },
    "userInfo": [ - "user"들의 정보를 리스트 형태로 담아서 보낼 것. 해당 애트리뷰트는 십진수 도(DD)로 표기된 소수점 6자리까지 위도/경도
        {
            "curLatitude": "37.511069",
            "curLongitude": "127.021327"
        }
    ],
    "areaInfo": [ - "area"는 유저들이 추가한 지역을 뜻함. address는 일반적인 구/동 정도까지, detailAddr은 말그대로 상세주소
        {
            "address":"서울특별시 강남구 역삼동",
            "detailAddr":""
        },
        {
            "address":"서울특별시 강남구 역삼동",
            "detailAddr":"671-3"
        },
        {
            "address":"강남",
            "detailAddr":""
        }
    ],
    "maxDistance": "0.3", - 중심위치로부터 반경 거리안의 모든 매장을 탐색(km단위) ex) 300m이내의 거리
    "minPoint": "3.0",    - 중심위치로부터 평점평균이 최소 ex) 3.0점 이상 매장만
    "maxPrice": "20000",  - 중심위치로부터 평균가격이 최대 20,000원까지만 검색
    "foodfilter": ""      - 거르는 음식은 미구현상태
}

# example
## 논현역 37.511069, 127.021327
## 신논현역 37.504526, 127.024445
## 강남역 37.497887, 127.027535

{
    "searchOptions": {
        "orderby": "avg_score",
        "searchType": "area",
        "searchNum": "many"
    },
    "userInfo": [
        {
            "curLatitude": "37.511069",
            "curLongitude": "127.021327"
        },
        {
            "curLatitude": "37.497887",
            "curLongitude": "127.027535"
        }
    ],
    "areaInfo": [
        {
            "address":"서울특별시 강남구 역삼동",
            "detailAddr":""
        },
        {
            "address":"서울특별시 강남구 역삼동",
            "detailAddr":"671-3"
        },
        {
            "address":"강남",
            "detailAddr":""
        }
    ],
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
        # init
        data = request.data
        errMessage =""
        curLatitude = curLongitude = 0
        maxDistance = str(data["maxDistance"])
        minPoint = str(data["minPoint"])
        maxPrice = str(data["maxPrice"])

        # SearchOptions is preprocessed.
        orderby = "distance" if(data["searchOptions"]["orderby"] == "") else (data["searchOptions"]["orderby"])
        if (orderby == "avg_score"):
            orderby += " desc"
        searchType = "user" if(data["searchOptions"]["searchType"] == "" or data["searchOptions"]["searchType"] == "user") else "area"
        searchNum = "one" if(data["searchOptions"]["searchNum"] == "" or data["searchOptions"]["searchNum"] == "one") else "many"
        
        # user
        # 현재 위치나 지정된 위치값을 받았다면
        if (searchType == "user"): 
            userList = data["userInfo"]
            # many people
            if searchNum == "many":
                for user in userList:
                    curLatitude += float(user["curLatitude"])
                    curLongitude += float(user["curLongitude"])
                curLatitude = str(round(curLatitude / len(userList),6))
                curLongitude = str(round(curLongitude / len(userList),6))

            # one people
            else :
                curLatitude = str(userList[0]["curLatitude"])
                curLongitude = str(userList[0]["curLongitude"])
        # area
        # 지역을 넣는다면 상세히 검색하지 않아도 가능.
        else : 
            areaList = data["areaInfo"]
            # many area
            if searchNum == "many":
                for area in areaList:
                    address = area["address"]
                    detailAddr = " "+area["detailAddr"] if (area["detailAddr"] != "") else "" 
                    # geocoding 
                    geoResponse = geoCoding(address+detailAddr)
                    geoData = geoResponse.json()
                    # error - 잘못된 주소값. 빈리스트로 반환
                    if(len(geoData["addresses"]) ==0): 
                        errMessage = "'"+address+"'는 주소가 잘못되었거나, 검색할 수 없는 지역입니다."
                        continue
                    else:
                        curLatitude += float(geoData["addresses"][0]["y"])
                        curLongitude += float(geoData["addresses"][0]["x"])
                curLatitude = str(round(curLatitude / len(areaList),6))
                curLongitude = str(round(curLongitude / len(areaList),6))
            # one area
            else:
                address = areaList[0]["address"]
                detailAddr = " "+areaList[0]["detailAddr"] if (areaList[0]["detailAddr"] != "") else "" 
                geoResponse = geoCoding(address+detailAddr)
                geoData = geoResponse.json()
                curLatitude = geoData["addresses"][0]["y"]
                curLongitude = geoData["addresses"][0]["x"]
 
        # sql
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
        
        # access db, excute sql and fetch data 
        mariadbConnection = mariadb.connect(user='root', password='ssafy', database='realpricedb', host="13.125.68.33")
        cursor = mariadbConnection.cursor()
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        merged_data =[
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        mariadbConnection.close()      
    
    response = {
        'count':len(merged_data),
        'result':merged_data,
        'errorMessage':errMessage
    }
    response['message']='검색된 맛집 추천 리스트입니다.' if response['count'] > 0 else '검색된 결과가 없습니다'
    return Response({'received_data':response})


    




