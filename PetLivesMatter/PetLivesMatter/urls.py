
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static



from PetRegistry import views

# from django.urls import include # Use include() to add URLS from the catalog application and authentication system


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('home/', home.site.urls),
]

# Have added url path to include petregistry urls - Tim
urlpatterns += [
    path('PetRegistry/', include('PetRegistry.urls')),
    #Added URL maps to redirect the base URL to our application - Tim
    path('', RedirectView.as_view(url='PetRegistry/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only) - Tim
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
