from django import forms

from .models import TrainRegModel


class AddTrainerReg(forms.ModelForm):
    class Meta:
        fields = ['time_slot', ]
        model = TrainRegModel
        labels = {
            'time_slot': 'Время тренировки',
        }


class AddReg(forms.ModelForm):
    class Meta:
        fields = ['time_slot', 'trainer', ]
        model = TrainRegModel
        labels = {
            'time_slot': 'Время тренировки',
            'trainer': 'Выберите тренера',
        }
