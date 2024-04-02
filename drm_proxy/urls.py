from django.contrib import admin
from django.urls import path
from .views import DRMProxyView, index_view

urlpatterns = [
    path("", index_view),
    path('admin/', admin.site.urls),
    path('drm_proxy/', DRMProxyView.as_view(),name='drm-proxy'),
]