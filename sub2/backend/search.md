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
    # response = json.dumps(response)
    # return HttpResponse(response, mimetype="application/json")
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