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

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', home_screen_view, name='home'),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
