"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('addpost/',views.addpost,name='addpost'),
    path('logout/',views.userlogout,name='logout'),
    path('updatepost/<int:id>/',views.updatepost,name='updatepost'),
    path('deletepost/<int:id>',views.deletepost,name='deletepost'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)