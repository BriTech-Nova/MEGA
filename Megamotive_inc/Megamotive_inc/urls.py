from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Customizing the Django admin site header and title

admin.site.site_header = "Admin Portal"        # Text at the top of the admin index page
admin.site.site_title = "Admin Portal"         # <title> tag of the admin pages
admin.site.index_title = "MEGAMOTIVE INC INSIGHTS" # Text at the top of the app list page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mega_motive.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)