from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

from .models import CheongsamModel, TeasetModel
from .serializers import CheongsamSerializers, TeasetSerializers

from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

# PRODUCT CONTENT CLASS

# Cheongsam Class
class CheongsamViewSet(viewsets.ModelViewSet):
    queryset = CheongsamModel.objects.all()
    serializer = CheongsamSerializers()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product-list.html'
    lookup_field = 'pk'

    # list all item
    # set order_by to prevent row re-order after edit
    def list(self, request):
        # get all product in order
        queryset = CheongsamModel.objects.order_by('id').all()

        # set context
        context = {'posts': queryset,
        'model': 'Cheongsam',
        }
        return Response(context)

    # serializer form
    def serializer_list(self, request):
        serializer = CheongsamSerializers()

        context = {
            'serializer': serializer,
        }
        return Response(context, template_name='product-create.html')

    def retrieve(self, request, pk):
        profile = get_object_or_404(CheongsamModel, pk=pk)
        serializer = CheongsamSerializers(profile)
        context = {
            'serializer': serializer,
        }
        return Response(context, template_name='product-edit.html')

    def delete_retrieve(self, request, pk):
        profile = get_object_or_404(CheongsamModel, pk=pk)
        serializer = CheongsamSerializers(profile)
        context = {
            'serializer': serializer,
        }
        return Response(context, template_name='product-delete.html')

    def create(self, request, *args, **kwargs):
        serializer = CheongsamSerializers()
        if request.method == 'POST':
            serializer = CheongsamSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print('status: status item create')
                return redirect('cheongsam')
            else:
                print('status: status bad item 404')
                print(serializer)
        return Response({'serializer': serializer})

    def update(self, request, pk):
        profile = get_object_or_404(CheongsamModel, pk=pk)
        serializer = CheongsamSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('status: status.Item Update')
            return redirect('cheongsam')
        else:
            print('status: status.Item Bad Update')

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return redirect('cheongsam')

    def perform_destroy(self, instance):
        instance.delete()


# Teaset Class
class TeasetViewSet(viewsets.ModelViewSet):
    queryset = TeasetModel.objects.all()
    serializer = TeasetSerializers()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product-list.html'
    lookup_field = 'pk'

    # list all item
    # set order_by to prevent row re-order after edit
    def list(self, request):
        # get all product in order
        queryset = TeasetModel.objects.order_by('id').all()

        context = {'posts': queryset,
        'model': 'Teaset',
        }
        return Response(context)

    # serializer form
    def serializer_list(self, request):
        serializer = TeasetSerializers()

        context = {
            'serializer': serializer,
        }
        return Response(context, template_name='product-create.html')

    def retrieve(self, request, pk):
        profile = get_object_or_404(TeasetModel, pk=pk)
        serializer = TeasetSerializers(profile)
        context = {
            'serializer': serializer,
        }
        return Response(context, template_name='product-edit.html')

    def delete_retrieve(self, request, pk):
        profile = get_object_or_404(TeasetModel, pk=pk)
        serializer = TeasetSerializers(profile)
        context = {
            'serializer': serializer,
        }
        return Response(context, template_name='product-delete.html')

    def create(self, request, *args, **kwargs):
        serializer = TeasetSerializers()
        if request.method == 'POST':
            serializer = TeasetSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print('status: status item create')
                return redirect('teaset')
            else:
                print('status: status bad item 404')
                print(serializer)
        return Response({'serializer': serializer})

    def update(self, request, pk):
        profile = get_object_or_404(TeasetModel, pk=pk)
        serializer = TeasetSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('status: status.Item Update')
            return redirect('teaset')
        else:
            print('status: status.Item Bad Update')

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return redirect('teaset')

    def perform_destroy(self, instance):
        instance.delete()
