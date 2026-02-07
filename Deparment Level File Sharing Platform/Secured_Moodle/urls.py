from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Admin panel
    path('@krmu_admin/', admin.site.urls, name='master'),
    # Public pages + dashboards
    path('', include('pages.urls')),
    # Authentication
    path('accounts/', include('accounts.urls')),

    # Future modules
    path('notes/', include('notes.urls')),
    path('assignments/', include('assignments.urls')),
    path('notifications/', include('notifications.urls')),
]

# Media file serving (development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
