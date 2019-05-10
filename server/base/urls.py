"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from material.frontend import urls as frontend_urls
from .views import index_view
from django.conf.urls.static import static
from django.conf import settings
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images import urls as wagtailimages_urls
from wagtail.core import urls as wagtail_urls

# import wechat_django


urlpatterns = [
    path('cms/admin/', include(wagtailadmin_urls)),
    path('cms/documents/', include(wagtaildocs_urls)),
    path('cms/images/', include(wagtailimages_urls)),
    path('cms/', include(wagtail_urls)),
    path('api/', include('api.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('site/admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('wx/', wechat_django.sites.wechat.urls),
    # path('app/control/', include(frontend_urls)),
    path('', index_view),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

