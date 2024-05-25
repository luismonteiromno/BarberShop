from django.urls import path

from .views import fileUpload, imageUpload

urlpatterns = [
    path("fileUpload/", fileUpload, name='file_upload'),
    path("imageUpload/", imageUpload, name='image_upload'),
]
