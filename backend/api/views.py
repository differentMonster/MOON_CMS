from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from products.models import CheongsamModel, TeasetModel
from products.serializers import CheongsamSerializers, TeasetSerializers

from cart.models import UserAccountModel, CartModel
from cart.serializers import UserSerializers, CartSerializers

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status

# RESTful API Class
#-------------------- accounts app -----------------------------------

class CartAPIViewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializers
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        cart = self.get_object()
        cart_serializers = self.get_serializer(cart)
        return Response(cart_serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = CartSerializers(data=request.data)
        if request.method == 'POST':
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data.errors, status=status.HTTP_400_BAD_REQUEST)


# Cheongsam API Class
# @api_view(['GET'])
class UsersAPIViewSet(viewsets.ModelViewSet):
    queryset = UserAccountModel.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        users = UserAccountModel.objects.all()
        users_serializer = self.get_serializer(users, many=True)
        return Response(users_serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializers(data=request.data)
        if request.method == 'POST':
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIViewSet(viewsets.ModelViewSet):
    queryset = UserAccountModel.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        user_serializers = self.get_serializer(user)
        return Response(user_serializers.data)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = get_object_or_404(UserAccountModel, pk=pk)
        self.perform_destroy(instance)
        return Response({'success': 'item has been deleted.'}, status=200)

    def perform_destroy(self, instance):
        instance.delete()


#-------------------- products app -----------------------------------

# Cheongsam API Class
# @api_view(['GET'])
class CheongsamAPIViewSet(viewsets.ModelViewSet):
    queryset = CheongsamModel.objects.all()
    serializer_class = CheongsamSerializers
    lookup_field = 'sku'

    # def get_queryset(self):
    #     return self.queryset

    # def get_object(self):
    #     sku_id = self.kwargs['sku']
    #     return self.get_queryset().filter(sku=sku_id)

    def list(self, request):
        products = CheongsamModel.objects.all()
        serializers = self.get_serializer(products, many=True)
        return Response(serializers.data)

    # def retrieve(self, request, pk=None):
    #     queryset = CheongsamModels.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = CheongsamSerializers(user)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)

    def post():
        pass


# Teaset API Class
# @api_view(['GET'])
class TeasetAPIViewSet(viewsets.ModelViewSet):
    queryset = TeasetModel.objects.all()
    serializer_class = TeasetSerializers
    lookup_field = 'sku'

    def list(self, request):
        products = TeasetModel.objects.all()
        serializers = self.get_serializer(products, many=True)
        return Response(serializers.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)

    def post():
        pass

# def cheongsam_products_list(request):
#     products = CheongsamModels.objects.all()
#     serializers = CheongsamSerializers(products, many=True)
#     return Response(serializers.data)

# @api_view(['GET'])
# def cheongsam_product_detail(request, pk):
#     products = CheongsamModels.objects.get(id=pk)
#     serializers = CheongsamAPISerializers(products)
#     return Response(serializers.data)
