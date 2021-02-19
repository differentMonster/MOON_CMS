from django.urls import path
from products.views import CheongsamViewSet, TeasetViewSet

# from rest_framework.urlpatterns import format_suffix_patterns

cheongsam_router_list = CheongsamViewSet.as_view({
'get': 'list',
})

cheongsam_router_create = CheongsamViewSet.as_view({
'get': 'serializer_list',
'post': 'create',
})

cheongsam_router_detail = CheongsamViewSet.as_view({
'get': 'retrieve',
'post': 'update',
})

cheongsam_router_delete = CheongsamViewSet.as_view({
'get': 'delete_retrieve',
'post': 'delete',
})

teaset_router_list = TeasetViewSet.as_view({
'get': 'list',
})

teaset_router_create = TeasetViewSet.as_view({
'get': 'serializer_list',
'post': 'create',
})

teaset_router_detail = TeasetViewSet.as_view({
'get': 'retrieve',
'post': 'update',
})

teaset_router_delete = TeasetViewSet.as_view({
'get': 'delete_retrieve',
'post': 'delete',
})

urlpatterns = [
    path('cheongsam/', cheongsam_router_list, name='cheongsam'),
    path('teaset/', teaset_router_list, name='teaset'),
    path('cheongsam/product_create/', cheongsam_router_create, name='cheongsam_create'),
    path('teaset/product_create/', teaset_router_create, name='teaset_create'),
    path(r'cheongsam/product_edit/<str:pk>/', cheongsam_router_detail, name='cheongsam_update'),
    path(r'teaset/product_edit/<str:pk>/', teaset_router_detail, name='teaset_update'),
    path(r'cheongsam/product_delete/<str:pk>/', cheongsam_router_delete, name='cheongsam_delete'),
    path(r'teaset/product_delete/<str:pk>/', teaset_router_delete, name='teaset_delete')
]
