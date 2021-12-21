from django.urls import path
from . import views

app_name="Turns"
urlpatterns = [
    path('',views.Turns_list,name='Turns_list'),
    path('amin/',views.Turns_list_amin,name='Turns_list_amin'),
    path('mehrdad/',views.Turns_list_mehrdad,name='Turns_list_mehrdad'),
    path('navid/',views.Turns_list_navid,name='Turns_list_navid'),
    path('nima/',views.Turns_list_nima,name='Turns_list_nima'),
    path('reservation',views.reservation_Turn,name='reservation'),
    path('<slug>',views.Turn_detail,name="detail"),
]
