from django.test import TestCase
from django.db.models import Q, Avg
from haversine import haversine
from .models import Store, Menu, Review
import json

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

def get_queryset(self):
    ulatitude = float(self['request']['ulatitude'])
    ulongitude = float(self['request']['ulongitude'])
    mlatitude = float(self['request']['mlatitude'])
    mlongitude = float(self['request']['mlongitude'])

    user_position = (ulatitude, ulongitude)
    map_position = (mlatitude, mlongitude)

    distance = haversine(user_position, map_position)

    distance_cost = int(cal_fee(distance)["bus_fee"])

    condition = (
        Q(latitude__range = (mlatitude - 0.01, mlatitude + 0.01)) |
        Q(longitude__range = (mlongitude - 0.015, mlongitude + 0.015))
    )

    store_infos = (
        Store
        .objects
        .filter(condition)
    )

    # menu_infos = (
    #     Menu
    #     .objects
    #     .prefetch_related('store')
    #     .all()
    # )

    # 근처 1km 이내 모든 식당 불러오기
    near_store_info = [info for info in store_infos
                        if haversine(map_position, (info.latitude, info.longitude)) <= 1]

    # 그 식당 중 리뷰 있는 식당 평균 가져오기
    review_infos = (
        Review
        .objects
        .prefetch_related('store')
        .filter(Q(store__in=near_store_info))
        .values('store')
        .annotate(Avg('score'))
        .order_by('-score__avg','store')
    )

    topStoreList = [review['store'] for review in review_infos]

    top_store_info = [info for info in near_store_info
                        if(info.id in topStoreList)]

    # print('리스트######################################', topStoreList)

    # review_infos = (
    #     Review
    #     .objects
    #     .prefetch_related('store')
    #     .filter(Q(store_id__in=near_store_info))
    #     .values('store')
    #     .annotate(Avg('score'))
    #     .order_by('store','-score')
    # )

    # menu_infos = (
    #     Menu
    #     .objects
    #     .prefetch_related('store')
    #     .filter(Q(store_id__in=near_store_info) & Q(price__range =(1,self['request']['price'])))
    #     .order_by("-price")
    # )

    # 평점이 높은 가게들의 모든 메뉴와 가게 정보를 가져온다. 근데 리뷰는 있고 그 가격 이하의 메뉴가 없는 집도 있다.
    menu_infos = (
        Menu
        .objects
        .prefetch_related('store')
        .filter(Q(store__in=top_store_info) & Q(price__range =(1,self['request']['price']-distance_cost)))
        .order_by('-price', 'store')
    )

    print(store_infos.query)
    print(menu_infos.query)
    print(review_infos.query)
    # print(top_store_info.query)

    print('근방 1km 안에 있는 음식점 수(리뷰, 메뉴 유무 노상관): ', len(near_store_info))
    print('리뷰가 있는 집의 수 (리뷰만 있고 메뉴 정보가 없을 수 있음 그래서 이거보다 작을 수 있음) : ', len(review_infos))
    print('리뷰가 있는 집의 총 메뉴 수 : ', len(menu_infos))
    # print(len(top_store_info))

    result = []
    dic_price = {}

    cnt = 1
    for menu in menu_infos:
        if menu.store.id in dic_price:
            store = dic_price.get(menu.store.id)
            if menu.price > store.get("price"):
                store["price"] = menu.price
                dic_price[menu.store.id] = store
        else:
            dic_price[menu.store.id] = {
                    "id": cnt,
                    "srcUrl": "www.google.com",
                    "address" : menu.store.address,
                    "latitude": menu.store.latitude,
                    "longitude": menu.store.longitude,
                    "storeName": menu.store.store_name,
                    "menu" : menu.menu_name,
                    "price": menu.price,
                    "distanceCost" : distance_cost,
                    "score": 0,
            }
            cnt += 1

    cnt = 1
    for row in review_infos:
        if row['store'] in dic_price:
            store = dic_price.get(row['store'])
            store["score"] = row["score__avg"]
            store["id"] = cnt
            result.append(store)
            cnt += 1

    print(self['request']['price'],'원 이하에', self['request']['ulongitude'], self['request']['ulatitude'], '근처 가게 수는', len(result), '개 입니다.')

    return menu_infos, review_infos, top_store_info, result



# stores, reviews, topStores, result = get_queryset({"request": {"price":10000, "ulatitude": 37.272618, "ulongitude":127.038970, "mlatitude": 37.535032, "mlongitude":126.991664,}}) # 수원 매탄동 173-89
# stores, reviews, topStores, result = get_queryset({"request": {"price": 10000, "ulatitude": 37.501235, "ulongitude": 127.039511, "mlatitude": 37.535032, "mlongitude": 126.991664,}})  # 역삼동 718-5
stores, reviews, topStores, result = get_queryset({"request": {"price":10000, "ulatitude": 37.272618, "ulongitude":127.038970, "mlatitude": 37.501235, "mlongitude":127.039511}}) # 수원 매탄동 173-89에서 역삼동 718-5 검색


# 37.272618, 127.038970  수원 내집

# cnt = 1
# print('근처 10000원 이하의 리뷰 top 음식점 리스트')
# for s in stores:
#     print('식당 ID : ', s.store.id, '식당명 : ', s.store.store_name, '\t주소 : ', s.store.address, '\t\t\t메뉴명 : ', s.menu_name, '\t\t\t가격 :', s.price)
#     # cnt += 1
#     # if (cnt > 100): break

# cnt = 1
# for r in reviews:
#     # print( '평점 평균 : ', r.score__avg, '\t리뷰 평점 : ', r.score,'\t식당명 : ', r.store.store_name, '\t주소 : ', r.store.address, '\t\t리뷰 내용 : ', r.content)
#     print(r)
#     # cnt += 1
#     # if (cnt > 100): break

# print('리뷰 top 음식점 리스트')
# for s in topStores:
#     print('식당명 : ', s.store.store_name, '\t주소 : ', s.store.address, '\t\t\t메뉴명 : ', s.menu_name, '\t\t\t가격 :', s.price)
#     cnt += 1
#     if (cnt > 100): break


store = {
    "1234":{
        "id": "1",
        "srcUrl": "www.google.com",
        "storeName": "할매 순대국",
        "menu" : "순대국밥",
        "price": 18000,
        "score": 4
    },
    "2345": {
        "id": "2",
        "srcUrl": "wwww.naver.com",
        "storeName": "스시 1290",
        "menu" : "광어 초밥 세트 10pc",
        "price": 19500,
        "score": 5
    }
}

# print(store.get("2345").get("price"))

for row in result:
    print(row)

# result_json = {
#     "stores":result
# }


# test = json.dumps(result_json)

# load_result = json.loads(test)
# print(load_result['stores'])