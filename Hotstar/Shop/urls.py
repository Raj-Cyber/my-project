from django.urls import path, include
from . import views

app_name = 'Shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:browser_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:browser_slug>/<slug:Prod_slug>/', views.ProdCatDetail,name='ProdCatDetail')

]