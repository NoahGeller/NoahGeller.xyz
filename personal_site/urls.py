from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from core import views as core_views

urlpatterns = [
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = core_views.error_404
handler500 = core_views.error_500
