from django.urls import path
from . import views
# from app.views import GenerateImageView

urlpatterns = [
    path('generate_image/', views.postAPI),
    path('post_image/', views.photoAPI),
]
