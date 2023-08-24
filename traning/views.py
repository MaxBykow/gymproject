from django.shortcuts import render
from django.views import View
from .models import TrainerInfo


# класс для рендеринга шаблона с тренерами
class Trainers(View):
    def get(self, request):
        trainers = TrainerInfo.objects.all()

        return render(request, 'traning/trainers.html', context={'trainers': trainers})

    def post(self, request):
        pass
