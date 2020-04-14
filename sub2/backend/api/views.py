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

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = SmallPagination
    queryset = Review.objects.all()

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

@api_view(['POST'])
def searchRealPrice(request, format=None):

    # a2 = Store.objects.filter(Review__store=149)
    storeList = Store.objects.all()
    reviewList = Review.objects.values('store').annotate(
        average = Avg('score')
    ).values('average', 'store')
    # print(reviewList)
    # print(a1.query)
    # print(a1)
    data = request.data
    print(reviewList)
    response = []
    # if request.method =='POST':w
    #     curLatitude = float(data["curLatitude"])
    #     curLongitude = float(data["curLongitude"])
    #     maxDistance = float(data["maxDistance"])
    #     minPoint = float(data["minPoint"])
    #     for store in storeList:
    #         if maxDistance >= haversine((store.latitude,store.longitude), (curLatitude,curLongitude), unit='km'):
    #             print(reviewList['store'].index(store.id))
                    
                    # if store.id == review['store'] and minPoint <= float(review['average']):
                    #     result = {}
                    #     result["id"] = store.id
                    #     result["store_name"] = store.store_name
                    #     result["branch"] = store.branch
                    #     result["category_list"] = store.category_list
                    #     result["rating"] = review['average']
                    #     if result not in response: 
                    #         response.append(result)
    
    print(response)
    # print(response[1].rating)
    return Response({'received data':request.data})
# 사용자 위치부터 최대반경 거리
# 최소별점
# 최소가격, 최대가격 받고
# 거르는 음식 기본 null값