"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from wishlist import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('wishlist/', include('wishlist.urls')),
    # path('wishlist/', include('wishlist.urls')),
    # path('xml/', views.show_xml, name='show_xml'),
    # path('json/', views.show_json, name='show_json'),
    # path('xml/<int:id>', views.show_xml_by_id, name='show_xml_by_id'),
    # path('json/<int:id>', views.show_json_by_id, name='show_json_by_id'), 

]
