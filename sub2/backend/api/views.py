from api import models, serializers
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Faq
from .models import Qna

class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StoreSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        name = self.request.query_params.get("name", "")
        queryset = (
            models.Store.objects.all().filter(store_name__contains=name).order_by("id")
        )
        return queryset


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FaqSerializer
    pagination_class = SmallPagination
    # queryset = Faq.objects.all()
    def get_queryset(self):
        return Faq.objects.all()
    
    # 1개 가져오는 함수 재정의
    # 객체를 검색 할 수 있으면 객체 200 OK의 직렬화 된 표현을 응답 본문으로 반환합니다 . 
    # 그렇지 않으면 404 Not Found를 반환합니다 
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response={
                    "data":serializer.data
                    ,"message":"해당 FAQ 반환"
                    ,"status" : status.HTTP_200_OK
                }
        return Response(response)
    # 여러개 가져오는 함수 재정의
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        message ="리스트가 없습니다" if len(queryset) == 0 else "FAQ 리스트 반환"
        data = queryset.values()
        response={
                    "data":data
                    ,"message":message
                    ,"status" : status.HTTP_200_OK
                }
        return Response(response)
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [AllowAny]
    #     return [permission() for permission in permission_classes]
    
class QnaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QnaSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        return Qna.objects.all()
    
    # 1개 가져오는 함수 재정의
    # 객체를 검색 할 수 있으면 객체 200 OK의 직렬화 된 표현을 응답 본문으로 반환합니다 . 
    # 그렇지 않으면 404 Not Found를 반환합니다 
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response={
                    "data":serializer.data
                    ,"message":"해당 Q&A 반환"
                    ,"status" : status.HTTP_200_OK
                }
        return Response(response)
    # 여러개 가져오는 함수 재정의
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        message ="리스트가 없습니다" if len(queryset) == 0 else "Q&A 리스트 반환"
        data = queryset.values()
        response={
                    "data": data
                    ,"message": message
                    ,"status" : status.HTTP_200_OK
                }
        return Response(response)
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [AllowAny]
    #     return [permission() for permission in permission_classes]
        
# from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.response import Response
class UserViewSet(viewsets.ModelViewSet):
# class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    pagination_class = SmallPagination
    def get_queryset(self):
        return User.objects.all()
    # lookup_field = "email"
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset.values(), many=True,context={'request': request})
    #     # message ="리스트가 없습니다" if len(queryset) == 0 else "유저 리스트 반환"
    #     data = list(serializer.data)
    #     print(data)
    #     response={
    #                 "data": data
    #                 ,"message": "message"
    #                 ,"status" : status.HTTP_200_OK
    #             }
    #     return Response(response)
    # def get_queryset(self):
    #     return User.objects.all()
    # # 1개 가져오는 함수 재정의
    # # 객체를 검색 할 수 있으면 객체 200 OK의 직렬화 된 표현을 응답 본문으로 반환합니다 . 
    # # 그렇지 않으면 404 Not Found를 반환합니다 
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object().filter(email=self.request.email)
    #     serializer = self.get_serializer(instance)
    #     response={
    #                 "data":serializer.data
    #                 ,"message":"해당 유저 반환"
    #                 ,"status" : status.HTTP_200_OK
    #             }
    #     return Response(response)
    # # 여러개 가져오는 함수 재정의
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     message ="리스트가 없습니다" if len(queryset) == 0 else "유저 리스트 반환"
    #     data = queryset.values()
    #     response={
    #                 "data": data
    #                 ,"message": message
    #                 ,"status" : status.HTTP_200_OK
    #             }
    #     return Response(response)
    # Add this code block
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = []#[AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

