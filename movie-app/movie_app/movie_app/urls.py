from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Actors/', include('Actors.urls')),
    path('Movies/', include('Movies.urls'))
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
