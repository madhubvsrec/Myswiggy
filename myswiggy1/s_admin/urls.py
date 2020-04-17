"""myswiggy1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from s_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.s_adminlogin,name='login'),
    path('logincheck/',views.logincheck,name='logincheck'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    #state

    path('open_state/',views.open_state,name='open_state'),
    path('save_state/',views.save_state,name='save_state'),
    path('state_update/',views.state_update,name='state_update'),
    path('update_state/',views.update_state,name='update_state'),
    path('state_delete/',views.state_delete,name='state_delete'),

    #city
    path('open_city/',views.open_city,name='open_city'),
    path('save_city/',views.save_city,name='save_city'),
    path('city_update/',views.city_update,name='city_update'),
    path('update_city/',views.update_city,name='update_city'),
    path('city_delete/',views.city_delete,name='city_delete'),

    #area
    path('open_area/', views.open_area, name='open_area'),
    path('save_area/', views.save_area, name='save_are'),
    path('area_update/', views.area_update, name='area_update'),
    path('update_area/', views.update_area, name='update_area'),
    path('area_delete/', views.area_delete, name='area_delete'),

]
