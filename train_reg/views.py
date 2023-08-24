from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from train_reg.forms import AddTrainerReg, AddReg
from train_reg.models import TrainRegModel
from traning.models import TrainerInfo


# класс-представление для записи к любому тренеру
class RegistrationTrain(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = AddReg()
            return render(request, 'train_reg/train_registration.html', context={'form': form})
        else:
            return HttpResponse('Вы не вошли в аккаунт!')

    def post(self, request):
        if request.user.is_authenticated:
            form = AddReg(request.POST, )
            if not TrainRegModel.objects.filter(time_slot=form.data['time_slot'],
                                                trainer=form.data['trainer']):
                tr = TrainerInfo.objects.get(id=form.data['trainer'])
                obj = TrainRegModel(trainer=tr,
                                    client=User.objects.get(username=request.user.username),
                                    is_booked=True, time_slot=form.data['time_slot']
                                    )
                obj.save()
                return HttpResponse('Запись успешно выполнена')
            else:
                return render(request, 'train_reg/train_registration.html', context={'form': form, 'flag': True,
                                                                                     'one': False})

        else:
            return HttpResponse('Вы не вошли в аккаунт!')


# класс-представление для записи к конкретному тренеру
class TrainRegView(View):
    def get(self, request, i):
        if request.user.is_authenticated:
            form = AddTrainerReg()
            tr = TrainerInfo.objects.get(id=i)
            return render(request, 'train_reg/train_registration.html', context={'form': form, 'flag': False,
                                                                                 'one': True, 'trainer': tr.name})
        else:
            return HttpResponse('Вы не вошли в аккаунт!')

    def post(self, request, i):
        if request.user.is_authenticated:
            form = AddTrainerReg(request.POST, )
            tr = TrainerInfo.objects.get(id=i)
            if not TrainRegModel.objects.filter(time_slot=form.data['time_slot'],
                                                trainer=tr):
                obj = TrainRegModel(trainer=tr,
                                    client=User.objects.get(username=request.user.username),
                                    is_booked=True, time_slot=form.data['time_slot']
                                    )
                obj.save()
                return HttpResponse('Запись успешно выполнена')
            else:
                return render(request, 'train_reg/train_registration.html', context={'form': form, 'flag': True,
                                                                                     'one': True, 'trainer': tr.name})

        else:
            return HttpResponse('Вы не вошли в аккаунт!')