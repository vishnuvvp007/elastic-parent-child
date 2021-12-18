
from django.urls import path
from . import views

urlpatterns = [
 path('',views.ApiUrls.as_view(),name="ApiUrls"),
 path('CategoryList',views.CategoryCreate.as_view(),name="CategoryList"),
#  path('es-search',views.BookCompoundSearchBackendDocumentViewSet.as_view(),name="es-search"),
#  path('VariantList',views.VariantList.as_view(),name="VariantList"),
]
