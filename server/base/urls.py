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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from material.frontend import urls as frontend_urls
from django.views import generic

# wagtail setting
# from wagtail.admin import urls as wagtailadmin_urls
# from wagtail.documents import urls as wagtaildocs_urls
# from wagtail.images import urls as wagtailimages_urls
# from wagtail.core import urls as wagtail_urls
# from wagtail.api.v2.endpoints import PagesAPIEndpoint
# from wagtail.api.v2.router import WagtailAPIRouter
# from wagtail.images.api.v2.endpoints import ImagesAPIEndpoint
# from wagtail.documents.api.v2.endpoints import DocumentsAPIEndpoint


# from .views import index_view
# import wechat_django

# wagtail与drf_yasg不兼容
# cms_api = WagtailAPIRouter('v2')
# cms_api.register_endpoint('pages', PagesAPIEndpoint)
# cms_api.register_endpoint('images', ImagesAPIEndpoint)
# cms_api.register_endpoint('documents', DocumentsAPIEndpoint)

urlpatterns = [
    re_path('^(:?app/)?login/?$', generic.RedirectView.as_view(url='accounts/login/', permanent=True)),
    path('app/', include(frontend_urls)),
    path('api/', include('api.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('site/admin/', admin.site.urls),
    path('', generic.RedirectView.as_view(url='app/dashboard', permanent=True)),
    # wagtail setting
    # path('cms/admin/', include(wagtailadmin_urls)),
    # path('cms/documents/', include(wagtaildocs_urls)),
    # path('cms/images/', include(wagtailimages_urls)),
    # path('cms/api/', cms.urls),
    # path('cms/', include(wagtail_urls)),
    # path('wx/', wechat_django.sites.wechat.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

