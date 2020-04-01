from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views
from .views import UserViewSet

router = DefaultRouter()#(trailing_slash=False)
router.register(r"stores", views.StoreViewSet, basename="stores")
router.register(r'users', UserViewSet)
# urlpatterns = router.urls
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]