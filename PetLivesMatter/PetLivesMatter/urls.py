
from django.contrib import admin
from django.urls import path
# from django.urls import include # Use include() to add URLS from the catalog application and authentication system


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home.site.urls),
]

# Have added url path to include petregistry urls - Tim
urlpatterns += [
    path('PetRegistry/', include('PetRegistry.urls')),
]
