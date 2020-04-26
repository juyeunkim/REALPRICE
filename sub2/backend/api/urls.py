from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()#(trailing_slash=False)
router.register(r"stores", StoreViewSet, basename="stores")
router.register(r"storeDetail", StoreDetailViewSet, basename="storedetails")
router.register(r"review", ReviewViewSet, basename="review")
router.register(r"faqs", FaqViewSet, basename="faqs")
router.register(r"qnas", QnaViewSet, basename="qnas")
router.register(r'users', UserViewSet)
router.register(r'reviews', ReviewViewSet, basename="reviews")
router.register(r'histories', HistoryViewSet, basename="histories")
router.register(r'menus', MenuViewSet, basename="menus")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^realprice/', searchRealPrice),
    url(r'^getStores/', getStores),
    url(r'^checkUsedEmail/(?P<email>[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',checkUsedEmail),
    url(r'^detailStore/(?P<id>[^/.]+)/$', detailStore)
]
#(?P)이 영역의 문자열에 정규표현식을 적용해서 data 라는 변수명으로 인자를 view로 넘기겠다.