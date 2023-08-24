from django import forms

from main_app.models import ImageSQL
from .models import TrainerInfo


class AddTrainer(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = TrainerInfo
        labels = {
            'picture': 'Картинка',
            'name': 'ФИО',
            'position': 'Должность',
            'description': 'Описание',
            'telephone': 'Телефон'
        }


class AddPic(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = ImageSQL
        labels = {
            'picture': 'Картинка',
            'title': 'название',

        }
