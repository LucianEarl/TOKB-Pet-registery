from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from PetRegistry import views
from django.views.generic import RedirectView
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
    path("register/", views.register, name="register"),  # <-- added
]

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
