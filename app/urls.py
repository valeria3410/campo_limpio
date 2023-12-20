from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mas_info/',views.mas_info,name='más información'),
    path('productores/',views.productores,),
    path('ingresos/',views.ingresos,name='ingresos'),
    path('ingresos/nuevo_ingreso/',views.nuevo_ingreso),
    path('retiros/',views.retiros, name='retiros'),
    path('retirar/<int:cod>',views.retirar),
]
