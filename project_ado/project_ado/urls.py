from django.contrib import admin
from django.urls import include, path

from .views import handler404, handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("unauth.urls")),
]

handler404 = "project_ado.views.handler404"
handler500 = "project_ado.views.handler500"
