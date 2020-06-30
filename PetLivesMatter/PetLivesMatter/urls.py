from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from PetRegistry import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from PetRegistry.views import (
    home_screen_view,
)

from account.views import(
    signup_view, user_detail,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
    path('pet_register/', views.pet_register_view, name="pet_register"),
    path('my_pets/', views.MyPetListView.as_view(), name="my_pets"),
    path('user_detail/', user_detail, name='user_detail'),
    path('pet/<int:pk>', views.PetDetailView.as_view(), name='pet_detail'),
    path('signup/', signup_view, name='signup'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

# Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
