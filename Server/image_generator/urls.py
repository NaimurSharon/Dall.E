from django.views.generic import TemplateView

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path('', TemplateView.as_view(template_name='index.html')),

]
