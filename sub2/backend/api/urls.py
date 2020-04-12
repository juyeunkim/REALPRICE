from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views
from .views import UserListView , UserView
# from .views import UserViewSet
router = DefaultRouter()#(trailing_slash=False)
# router.register(r"stores", views.StoreViewSet, basename="stores")
# router.register(r"faqs", views.FaqViewSet, basename="faqs")
# router.register(r"qnas", views.QnaViewSet, basename="qnas")
# router.register(r'users', UserViewSet, basename="users")

urlpatterns = router.urls
# urlpatterns = router.urls
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    # url(r'^$', api_root),
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^users/$', UserListView.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserView.as_view()),
    # url(r'^users/$', UserList.as_view(),name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(),name='user-detail'),
]
# urlpatterns += format_suffix_patterns([
#     # API to map the student record
#     url(r'^users/$',
#         views.UserProfileView.as_view(),
#         name='user-list'),
# ])