"""petadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from client import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.showindex, name='showindex'),
    url('insertCustomerDetails', views.insertCustomerDetails, name='insertCustomerDetails'),
    url('insertCustomerOrderDetails', views.insertCustomerOrderDetails, name='insertCustomerOrderDetails'),
    url('insertOwnerDetails', views.insertOwnerDetails, name='insertOwnerDetails'),
    url('insertCustomerPetBooking', views.insertCustomerPetBooking, name='insertCustomerPetBooking'),
    url('insertCustomerPetDetails', views.insertCustomerPetDetails, name='insertCustomerPetDetails'),
    url('insertCustomerProductDetails', views.insertCustomerProductDetails, name='insertCustomerProductDetails'),
    url('login', views.login, name='login'),
    url('CustomerOrderDetails_views_A', views.CustomerOrderDetails_views_A, name='CustomerOrderDetails_views_A'),
    url('CustomerOrderDetails_views_S', views.CustomerOrderDetails_views_S, name='CustomerOrderDetails_views_S'),
    url('CustomerDetails_views_A', views.CustomerDetails_views_A, name='CustomerDetails_views_A'),
    url('CustomerDetails_views_S', views.CustomerDetails_views_S, name='CustomerDetails_views_S'),
    url('OwnerDetails_views_A', views.OwnerDetails_views_A, name='OwnerDetails_views_A'),
    url('OwnerDetails_views_C', views.OwnerDetails_views_C, name='OwnerDetails_views_C'),
    url('CustomerPetBooking_views_A', views.CustomerPetBooking_views_A, name='CustomerPetBooking_views_A'),
    url('CustomerPetBooking_views_S', views.CustomerPetBooking_views_S, name='CustomerPetBooking_views_S'),
    url('CustomerPetDetails_views_A', views.CustomerPetDetails_views_A, name='CustomerPetDetails_views_A'),
    url('CustomerPetDetails_views_C', views.CustomerPetDetails_views_C, name='CustomerPetDetails_views_C'),
    url('CustomerProductDetails_views_A', views.CustomerProductDetails_views_A, name='CustomerProductDetails_views_A'),
    url('CustomerProductDetails_views_C', views.CustomerProductDetails_views_C, name='CustomerProductDetails_views_C'),
    url('userlogin_views', views.userlogin_views, name='userlogin_views'),
    url('changepass', views.changepass, name='changepass'),
    url('Admin_home', views.Admin_home, name='Admin_home'),
    url('Staff_home', views.Staff_home, name='Staff_home'),
    url('Customer_home', views.Customer_home, name='Customer_home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
