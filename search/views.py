from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from .serializer import *
from .documents import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status,generics
from rest_framework.generics import ListAPIView
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser
from django_elasticsearch_dsl_drf.filter_backends import (
   DefaultOrderingFilterBackend,
   CompoundSearchFilterBackend,
   OrderingFilterBackend,
)

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

class ApiUrls(APIView):
        def get(self, request):
              api_urls ={

                 'CategoryList':'/CategoryList/',
                 'GroupList':'/GroupList/',
                 'VariantList':'/VariantList/',
              }
              return Response(api_urls)

class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookCompoundSearchBackendDocumentViewSet(DocumentViewSet):
   document = CategoryDocument
   serializer_class = CategorySerializer
   lookup_field = 'id'

   filter_backends = [
         # ...
         OrderingFilterBackend,
         DefaultOrderingFilterBackend,
         CompoundSearchFilterBackend,
         # ...
   ]
   multi_match_search_fields = (
      'name',
      'status',
   )