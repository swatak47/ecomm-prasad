from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.models import User ,auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home,name="Home"),
    path("contact-us/", views.contact, name="contact"),
    path("login",views.log_in,name="log_in"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact-info/', views.contact_info, name='contact_info'),
    path('farm/',views.farmer,name="farmer"),
    path('farm_login/',views.farmer_log,name="farmer_log"),
    path('farmer_info/',views.farmer_info,name="farmer_info"),
    path('farmer_profile/',views.farmer_ui,name="farmer_ui"),
    path('customer/',views.customer,name="customer"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('delete_record/<int:id>/', views.delete_record, name ='delete_record'),
    path('customer_login/', views.customer_login,name="customer_login"),
    path('farmer_log/',views.farmer_log,name="farmer_log"),
    
    

]