"""
URL configuration for que project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('printers/', include('printers.urls', namespace='printers')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls', namespace='api')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('api-token-auth/', views.obtain_auth_token),
]
