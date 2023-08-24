from django.contrib import admin
from django.urls import path, include
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('create_reg/', v.RegistrationTrain.as_view(), name='createreg'),
                  path('trainer_reg/<int:i>/', v.TrainRegView.as_view(), name='trainerreg'),
                  # path('download/', v.DownloadImage.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
