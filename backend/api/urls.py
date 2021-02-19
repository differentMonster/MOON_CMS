from django.urls import path, include
from . import views
from django.conf.urls import *
from api.views import CheongsamAPIViewSet,TeasetAPIViewSet, UsersAPIViewSet, UserDetailAPIViewSet, CartAPIViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin


cheongsam_api_list = CheongsamAPIViewSet.as_view({
'get': 'list'
})

cheongsam_api_detail = CheongsamAPIViewSet.as_view({
'get': 'retrieve'
})

teaset_api_list = TeasetAPIViewSet.as_view({
'get': 'list'
})

teaset_api_detail = TeasetAPIViewSet.as_view({
'get': 'retrieve'
})

accounts_list_api = UsersAPIViewSet.as_view({
'get': 'list',
'post': 'post',
})

account_detail_api = UserDetailAPIViewSet.as_view({
'get': 'retrieve',
'post': 'delete'
})

cart_list_api = CartAPIViewSet.as_view({
'get': 'retrieve',
'post': 'post'
})

urlpatterns = [
    # path(r'token/', TokenObtainPairView.as_view(), name='token'),
    # path(r'refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('admin/', admin.site.urls),
    path('auth/',include('djoser.urls')), #add
    path('auth/',include('djoser.urls.jwt')), #add
    path(r'cheongsam/', cheongsam_api_list, name='api-cheongsam'),
    path(r'teaset/', teaset_api_list, name='api-teaset'),
    # path(r'auth/user/', accounts_list_api, name='api-accounts'),
    path(r'cheongsam/<str:sku>/', cheongsam_api_detail, name='api-cheongsam-detail'),
    path(r'teaset/<str:sku>/', teaset_api_detail, name='api-teaset-detail'),
    path(r'account/<int:pk>/', account_detail_api, name='api-account-detail'),
    path(r'account/<int:pk>/cart/', cart_list_api, name='api-cart-detail'),
    # url(r'^cheongsam/(?P<sku>[-\w\d]+)/$', cheongsam_api_list, name='api-detail'),
    # url(r'^cheongsam/(?P<slug>[-\w\d]+)/$', cheongsam_api_detail, name='api-detail'),
]
