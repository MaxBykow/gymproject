from django import forms

from main_app.models import CommentModel
from traning.models import TrainerInfo


class ImageForm(forms.Form):
    picture = forms.FileField()


# класс формы для создание комментариев на главной странице
class CommentaryForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.Textarea)
