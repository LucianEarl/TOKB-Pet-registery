from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from PetRegistry import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
]

<<<<<<< HEAD
urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
    path('accounts/', include('django.contrib.auth.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

=======
>>>>>>> 768d0e086db9184e57729ef230e796b5651ba598
#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
