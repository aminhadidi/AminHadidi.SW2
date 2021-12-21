from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about,name='about'),
    path('',views.home,name='home'),
    path('turns/',include('Turns.urls')),
    path('accounts/',include('accounts.urls'))

]

urlpatterns += staticfiles_urlpatterns()
