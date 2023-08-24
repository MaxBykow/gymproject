from django.contrib import admin
from django.urls import path, include
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('home/', v.base, name='main'),
                  path('write/', v.CommentaryAdd.as_view(), name='add_comment'),
                  path('download/', v.DownloadImage.as_view()),
                  path('gallery/', v.Gallery.as_view(), name='gym_gallery'),
                  path('trainers/', include('traning.urls')),
                  path('download_pic/', v.DownloadPic.as_view()),
                  path('contacts/', v.contacts, name='contacts'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
