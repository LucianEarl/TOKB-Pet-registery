# from django.urls import path
#
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('donate/', views.donate, name='donate'),
# ]
#
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url
# from django.urls import include
# from PetRegistry import views
# from django.views.generic import RedirectView
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
# ]
#
# urlpatterns += [
#     path('home/', include('home.urls')),
# ]
#
# urlpatterns += [
#     path('', RedirectView.as_view(url='/home/')),
# ]
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
# #Add Django site authentication urls (for login, logout, password management)
#
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
