from django.urls import path
from . import views


urlpatterns = [
    path('',views.Turns_list),
    path('amin/',views.Turns_list_amin),
    path('mehrdad/',views.Turns_list_mehrdad),
    path('navid/',views.Turns_list_navid),
    path('nima/',views.Turns_list_nima),
]
