from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import CommentaryForm
# from .forms import ImageForm
from .models import ImageSQL, CommentModel
from traning.models import TrainerInfo
from traning.forms import AddTrainer, AddPic


# Create your views here.
def base(request):
    images = ImageSQL.objects.all()
    comments = CommentModel.objects.order_by('-data')
    return render(request, 'main_app/base_page.html', context={'pic': images, 'comments': comments})


class DownloadImage(View):  # для добавления тренера
    def get(self, request):
        form = AddTrainer()
        return render(request, 'main_app/download_pic.html', context={'form': form})

    def post(self, request):
        form = AddTrainer(request.POST, request.FILES)
        if form.is_valid():
            obj = TrainerInfo(picture=form.cleaned_data['picture'], name=form.cleaned_data['name'],
                              position=form.cleaned_data['position'], description=form.cleaned_data['description'])
            obj.save()
            return render(request, 'main_app/ok.html')
        return render(request, 'main_app/download_pic.html', context={'form': form})

class DownloadPic(View):
    def get(self, request):
        form = AddPic()
        return render(request, 'main_app/download_pic.html', context={'form': form})

    def post(self, request):
        form = AddPic(request.POST, request.FILES)
        if form.is_valid():
            obj = ImageSQL(title=form.cleaned_data['title'], picture=form.cleaned_data['picture'])
            obj.save()
            return render(request, 'main_app/ok.html')


class Gallery(View):
    def get(self, request):
        images1 = ImageSQL.objects.all()
        images1 = images1[:6]
        return render(request, 'main_app/gym_parts.html', context={'pics1': images1})

    def post(self, request):
        pass


class CommentaryAdd(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = CommentaryForm()
            return render(request, 'main_app/add_comment.html', context={'form': form})
        else:
            return HttpResponse('Вы не вошли в аккаунт!')

    def post(self, request):
        if request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            if form.is_valid():
                # дописать
                obj = CommentModel(text=form.cleaned_data['text'],
                                   author=User.objects.get(username=request.user.username))
                obj.save()
                return HttpResponse('Комментарий сохранен')
            return render(request, 'main_app/add_comment.html', context={'form': form})
        else:
            return HttpResponse('Вы не вошли в аккаунт!')


# Create your views here.
def contacts(request):
    image = ImageSQL.objects.all()
    image = image[6]
    return render(request, 'main_app/contacts.html', context={'pic': image})

