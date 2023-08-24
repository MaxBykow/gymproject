from django.urls import path, include
from . import views as v


urlpatterns = [
    path('', v.Trainers.as_view(), name='all_trainers'),
]
