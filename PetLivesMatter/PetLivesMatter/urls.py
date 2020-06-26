from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from PetRegistry import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
    path('signup/', views.signup_view, name="signup"),
    path('pet_register/', views.pet_register_view, name="pet_register"),
    path('my_pets/', views.MyPetListView.as_view(), name="my_pets"),
    path('pet/<int:pk>', views.PetDetailView.as_view(), name='pet_detail')
]


# Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
