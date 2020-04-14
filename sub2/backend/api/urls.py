from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *#StoreViewSet,UserViewSet, FaqViewSet, QnaViewSet


router = DefaultRouter()#(trailing_slash=False)
router.register(r"stores", StoreViewSet, basename="stores")
router.register(r"review", ReviewViewSet, basename="review")
router.register(r"faqs", FaqViewSet, basename="faqs")
router.register(r"qnas", QnaViewSet, basename="qnas")
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^realprice/', searchRealPrice),
]
