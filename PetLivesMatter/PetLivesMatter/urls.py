"""PetLivesMatter URL Configuration

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
# from django.urls import include # Use include() to add URLS from the catalog application and authentication system


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home.site.urls),
]

# Have added url path to include petregistry urls - Tim
# urlpatterns += [
#     path('PetRegistry/', include('PetRegistry.urls')),
# ]
