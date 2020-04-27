# realprice api version


1. use python library 
 - haversine library을 통한 반경 거리 계산
 - 전체 객체를 불러 처리하고, django에서 서브처리를 하느라 너무 느리다

```python
@api_view(['POST'])
def searchRealPrice(request):#, format=None):
# 거리 : 반경 x km 이내 (현재 위치든 다른 곳이든 위치를 받아야함)
# 맛   : 각 가게의 리뷰점수를 평균내서 순위매긴 값이 유저가 원하는 최소 평점 수치 y보다 높아아야함
# ---현재 여기까지
# ---문제 전체 호출 한번해서 너무 느림 - 쿼리로 좀 축소해서 가져오고 싶은데 마음대로 못 다루겠음
# 메뉴가 없어서 진행을 더이상 할 수가 없음!! 어쨌든 현재 할 수 있는 상태에서 효율적인 방법을 찾아보겠음
# 가격 : 메뉴 추출해서 작업하고 있어야함...
# 거르는 음식 : 메뉴 이름정도로 거르던지 해야하는 상태... -> 이걸로 가게를 거르긴 좀..
# 후에 웨이팅 시간이 추가된다면 
    storeList = Store.objects.all()
    # 대표 메뉴의 가격 or 평균가격이 매겨지면 filtering 처리하면 좀 더 빠르긴 할 것
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
                    result["area"] = store.area
                    result["address"] = store.address
                    result["tel"] = store.tel
                    result["category_list"] = store.category_list
                    result["latitude"] = store.latitude
                    result["longitude"] = store.longitude
                    result["rating"] = review[0]['average']
                    if result not in merged_data: 
                        merged_data.append(result)
    merged_data = sorted(merged_data, key=lambda data: data['rating'], reverse=True)          
    response = {
        'count':len(merged_data),
        'result':merged_data,
    }
    response['message']='검색된 맛집 추천 리스트입니다.' if response['count'] > 0 else '검색된 결과가 없습니다'
    return Response({'received_data':response})

# 사용자 위치부터 최대반경 거리
# 최소별점
# 최소가격, 최대가격 받고
# 거르는 음식 기본 null값
```
```json
{
	"searchOptions":{
	   	"orderby": "avg_score",
		"searchType":"user",
		"searchNum":"one",
	},
	"userInfo":[
		{
			"curLatitude": "37.503652",
			"curLongitude": "127.038125"
		},
        {
			"curLatitude": "38.503652",
			"curLongitude": "127.038125"
		}
	],
	"areaInfo":[

	],
	"maxDistance": "0.3",
	"minPoint": "3",
	"maxPrice": "20000",
	"foodfilter": ""
}
```

2. 개인 User Version

```python
# 개인유저 버전
@api_view(['POST'])
def searchRealPrice(request):
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
    #     # 여기서 숫자가 1명이면 그대로 진행하면 되고 1지역이면 네이버api를 이용해서 curLatitude, curLongitude 변경해줘야함
    #     # 여기서 숫자가 여러명이면 평균값 구하기. 일부 사람 수 제외 시는 프론트에서 제어해주는게 좋을듯
    #     #              여러지역이면 각 지역별로 네이버 api 이용해서 구한 뒤, 평균값인데
    #     # 실제로 사용자가 이용한다고 했을때,
    #     #        다른 유저들의 위치정보를 상세하게는 알 수 없을 것인데, 네이버api가 가능해지면 전부다 주소로 입력받아서 할지
    #     #        각자 자신 위치를 설정할 수 있게 할 것인지. 미리 각자 주소를 등록해두게 할 것인지 결정해야함
    #     # 따라서 일단 네이버api로 주소를 좌표값으로 바꾸는 geocoding 하도록 할 것
        # print(curLatitude, curLongitude)
```
    
3. 여러 지역, 여러 유저 커버 version
```json
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
```

```python
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

```