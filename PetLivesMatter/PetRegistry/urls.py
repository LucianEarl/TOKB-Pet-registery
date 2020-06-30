from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from PetRegistry import views
from django.views.generic import RedirectView

from PetRegistry.views import (
    home_screen_view,)
"""
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, Path
    2. Add a URL to urlpatterns: path('blog/', Include('blog.urls'))
"""

urlpatterns = [
""" File Path PetRegistry #
"""
    path('<SPECIES_CHOICES:pk>', views.pet_detail, name='detail'),
"""
"""
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', home_screen_view, name='home'),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
