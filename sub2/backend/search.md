# **Realprice Search Api Version**

## **INDEX**
- [파이썬 라이브러리로 처리](#Use-Python-Library)
- [개인 User의 현재 위치](#개인-User의-현재-위치)
- [여러 지역 검색 및 여러 명의 유저 위치](#여러-지역-검색-및-여러-명의-유저-위치)
- [가격과 현재위치, 반경으로만 검색](#가격과-현재위치-반경으로만-검색)

## **Use Python Library**

 - 위치, 반경 거리, 최소 평점을 받아서 검색결과 반환
 - haversine library을 통한 반경 거리 계산
 - annotate를 통해 그룹 별 평점을 취하고, lambda로 리뷰점수 filtering
 - 전체 객체를 불러 처리하고, django에서 서브처리를 하느라 너무 느리다

 - 조건
    |거리|맛|
    |-|-|
    |반경 x km 이내 (현재 위치든 다른 곳이든 위치를 받아야함)|각 가게의 리뷰점수를 평균내서 순위매긴 값이 유저가 원하는 최소 평점 수치 y보다 높아아야함|

 - 현재까지 문제
   - 매장 전체를 호출해서 너무 느리고 쿼리로 축소하고 싶은데 마음대로 못하겠던 상황
   - 메뉴를 넣지 않아서 진행 불가한 상태
   - 대표 메뉴의 가격이나 평균가격등을 이용해야함
   - 거르는 음식을 메뉴 이름정도로 거르던지 해야하는 상태 
   - 웨이팅 시간 추가 문제

 - python code
```python
@api_view(['POST'])
def searchRealPrice(request):#, format=None):
 
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

## **개인 User의 현재 위치**

- 개인 유저의 위치, 반경거리, 평점, 가격, 정렬방식을 받아서 검색결과를 반환
- SQL 쿼리를 직접 이용하여 복잡한 내용을 처리함 => 훨씬 빨라짐 


- 지역 검색, 여러명 검색 등을 고려
  - 숫자가 1명이면 그대로 진행하면 되고 1지역이면 네이버api를 이용해서 curLatitude, curLongitude 변경해줘야함
  - 숫자가 여러명이면 평균값 구하기. 일부 사람 수 제외 시는 프론트에서 제어해주는게 좋을듯
  - 여러지역이면 각 지역별로 네이버 api 이용해서 구한 뒤, 평균값인데
  - 실제로 사용자가 이용한다고 했을때, 다른 유저들의 위치정보를 상세하게는 알 수 없을 것인데, 네이버api로 전부 다 주소로 입력받아서 할지/각자 자신 위치를 설정할 수 있게 할 것인지. 미리 각자 주소를 등록해두게 할 것인지 결정해야함
  - 따라서 일단 네이버api로 주소를 좌표값으로 바꾸는 geocoding 하도록 할 것

- POST 요청 파라미터    
```json
{
    "curLatitude": "37.503652",
    "curLongitude": "127.038125",
	"maxDistance": "0.3",
	"minPoint": "3",
	"maxPrice": "20000",
	"foodfilter": "",
    "orderby": "avg_score"
}
```
- python code
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
    
```
    
## **여러 지역 검색 및 여러 명의 유저 위치**

- searchOptions으로 1명, 1지역, n명, n지역과 정렬방식에 대한 정보를 취함
- userInfo와 areaInfo는 필요한 부분만 넘기고 searchOptions을 통해서 백엔드에서 판단하여 처리
- 그 외는 동일하며, n명과 n지역은 평균 위도/경도를 만들어서 계산에 활용
- 기존 SQL을 최대한 활용하면서, 다양한 부분을 케어할 수 있도록 구현하였고 속도도 괜찮음

- POST 요청파라미터 형식 및 예시
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
- python code
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

## **가격과 현재위치 반경으로만 검색**

 - 프로젝트 진행상황에 맞게 요청파라미터를 축소
 - 개인/모임 유저, 지역/여러지역 버전에서 가격, 평점 파라미터 제거, 가격순 정렬 or 평점순 정렬은 가능
 - 매장과 현 위치의 거리를 교통비 계산에 이용하고 더해서 결과 반환
 - 교통비는 주유비, 버스비, 택시비를 실제 기준에 맞춰 작성했으며, 기본적인 realprice 값은 버스를 1회 타고 간다고 가정

 - 검색범위가 증가함에 따른 매장 수 급증 문제
   - 반환된 리스트를 페이징 처리?
   - 매 위치마다 다른 POST를 날려야하기 때문에 PAGING을 위한 GET을 만들 수 없음
   - 모델로 만들어 최근위치를 저장한다면 가능하겠지만, 검색된 모든 매장이 한번에 맵에 나와야함
   - 사용자가 현 위치에서 15km이상 떨어진 곳을 검색하고자 하는 것이 아니라, 15km떨어진 곳에서 주변을 검색하는 것이 일반적인 상황이라 판단되며, 굳이 그렇게 많이 본다면 맵에 수 천개 이상의 매장이 나와야하므로 시간이 일부 소요되는 것은 성능적인 문제라고 판단하기 어렵다. 
   - 따라서 페이징 처리는 하지 않는편이 낫다고 판단.

 - 지역검색은 추후 활용가능하므로 남김

```json
{
    "searchOptions": {
        "orderby": "avg_score",
        "searchType": "user", 
        "searchNum": "one"
    },
    "userInfo": [ 
        {
            "curLatitude": "37.511069",
            "curLongitude": "127.021327"
        }
    ],
    "areaInfo": [ 
        {
            "address":"서울특별시 강남구 역삼동",
            "detailAddr":""
        }
    ],
    "maxDistance": "1", 
    "foodfilter": "" 
}
```
- python code
```python
@api_view(['POST'])
def searchRealPrice(request):
    if request.method =='POST':
        # init
        data = request.data
        errMessage =""
        curLatitude = curLongitude = 0
        maxDistance = str(data["maxDistance"])

        # SearchOptions is preprocessed.
        orderby = "distance" if(data["searchOptions"]["orderby"] == "") else (data["searchOptions"]["orderby"])
        if (orderby == "avg_score"):
            orderby += " desc"
        searchType  = "user" if(data["searchOptions"]["searchType"] == "" or data["searchOptions"]["searchType"] == "user") else "area"
        searchNum   = "one"  if(data["searchOptions"]["searchNum"]  == "" or data["searchOptions"]["searchNum"]  == "one")  else "many"
        
        # user
        # 현재 위치나 지정된 위치값을 받았다면
        if (searchType == "user"): 
            userList = data["userInfo"]
            # many people
            if searchNum == "many":
                for user in userList:
                    curLatitude  += float(user["curLatitude"])
                    curLongitude += float(user["curLongitude"])
                curLatitude      = str(round(curLatitude / len(userList),6))
                curLongitude     = str(round(curLongitude / len(userList),6))

            # one people
            else :
                curLatitude  = str(userList[0]["curLatitude"])
                curLongitude = str(userList[0]["curLongitude"])
        # area
        # 지역을 넣는다면 상세히 검색하지 않아도 가능. - 확장 가능성을 두고 냅두자 일단
        else : 
            areaList = data["areaInfo"]
            # many area
            if searchNum == "many":
                for area in areaList:
                    address     = area["address"]
                    detailAddr  = " "+area["detailAddr"] if (area["detailAddr"] != "") else "" 
                    # geocoding 
                    geoResponse = geoCoding(address+detailAddr)
                    geoData = geoResponse.json()
                    # error - 잘못된 주소값. 빈리스트로 반환
                    if(len(geoData["addresses"]) ==0): 
                        errMessage = "'"+address+"'는 주소가 잘못되었거나, 검색할 수 없는 지역입니다."
                        continue
                    else:
                        curLatitude  += float(geoData["addresses"][0]["y"])
                        curLongitude += float(geoData["addresses"][0]["x"])
                curLatitude  = str(round(curLatitude / len(areaList),6))
                curLongitude = str(round(curLongitude / len(areaList),6))
            # one area
            else:
                address      = areaList[0]["address"]
                detailAddr   = " "+areaList[0]["detailAddr"] if (areaList[0]["detailAddr"] != "") else "" 
                geoResponse  = geoCoding(address+detailAddr)
                geoData      = geoResponse.json()
                curLatitude  = geoData["addresses"][0]["y"]
                curLongitude = geoData["addresses"][0]["x"]
        
        # sql
        sql = "SELECT s.*, ROUND(AVG(m.price),0) AS avg_price, COUNT(m.id) AS cnt_menu\
                FROM\
                    (SELECT\
                    s.*,\
                    ROUND(AVG(r.score),3) AS avg_score,\
                    COUNT(r.id) AS cnt_review,\
                    ROUND((6371\
                        *ACOS(\
                        (COS(RADIANS("+curLatitude+"))*COS(RADIANS(s.latitude))*COS(RADIANS(s.longitude)-RADIANS("+curLongitude+")))+\
                        (SIN(RADIANS("+curLatitude+"))*SIN(RADIANS(s.latitude))))\
                    ),3) AS distance\
                    FROM api_store AS s\
                    JOIN api_review AS r\
                    ON s.id = r.store\
                    GROUP BY s.id\
                    HAVING distance < "+maxDistance+") s\
                JOIN api_menu m\
                ON s.id = m.store\
                GROUP BY m.store\
                order by "+orderby+";"
        
        # access db, excute sql and fetch data 
        mariadbConnection = mariadb.connect(user='root', password='ssafy', database='realpricedb', host="13.125.68.33")
        cursor = mariadbConnection.cursor()
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        merged_data =[
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        for store in merged_data:
            store['transportation'] = cal_fee(store['distance'])
            # 뭐 더할지는 아직 모르겠고
            store['realprice'] = str(float(store['avg_price']) + float(store['transportation']['bus_fee']))
        # 진짜 가격 합
        mariadbConnection.close()      
    
    response = {
        'count':len(merged_data),
        'result':merged_data,
        'errorMessage':errMessage
    }
    response['message']='검색된 맛집 추천 리스트입니다.' if response['count'] > 0 else '검색된 결과가 없습니다'
    # 너무 먼거리는 양이 많아서 페이징 처리를 해야하지만 맵에 전부 표시되는 것도 필요하니까 다 주긴 해야지
    return Response({"received_data":response})
```
- 교통비 계산
```python
def cal_fee(distance):
    #일단은 디폴트로 이렇게하고 기본연비 + 휘발유 -> 나중에 좀 더 깊게
    fuel_efficiency = 24.3  # km/L 연비
    gasoline = 1292.00      # won/L 휘발유
    diesel = 1102.67        # won/L 경유
    lpg = 816.94            # won/L
    car_msg = "2020.04.23 기준 유가 "+str(gasoline)+"원/L (한국석유공사 opinet) 본 가격정보는 특정 시점에 수집된 전국 평균 가격으로 실제 판매가격과 다를 수 있습니다."
    # 1km당 41.15ml 그리고 53.16원이 소요됨
    car_fee = distance * 53.16
    # bus - 환승시 : 기본요금(10km)까지 + 추가 5km마다 100원씩 추가요금 
    bus_msg = "서울시 시내버스 요금 체계 - 일반(교통카드) 및 추가 5km 당 환승요금 붙는 것으로 계산한 가격으로 실제가격은 이와 다를 수 있습니다."
    bus_fee = 1200
    if distance > 10:
        remain = distance-10
        while(remain > 0):
            remain -=5
            bus_fee += 100

    # taxi - 서울시의 택시요금 체계 / 주간, 중형택시 요금체계에 따름
    taxi_msg = "서울시 택시요금 체계 - 주간/중형택시 요금체계에 따른 가격으로 실제가격은 이와 다를 수 있습니다."
    taxi_fee = 3800
    if distance > 2:
        remain = distance-2
        while(remain > 0):
            remain-=0.132
            taxi_fee += 100
    result = {
        "car_fee"   :str(car_fee),
        "car_msg"   :str(car_msg),
        "bus_fee"   :str(bus_fee),
        "bus_msg"   :str(bus_msg),
        "taxi_fee"  :str(taxi_fee),
        "taxi_msg"  :str(taxi_msg),
    }
    return result
```