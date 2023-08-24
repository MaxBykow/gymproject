from django.db import models


# Create your models here.

class TrainerInfo(models.Model):

    POSITION = [
        ('1', 'Главный тренер'),
        ('2', 'Дежурный тренер'),
        ('3', 'Тренер по единоборствам'),
        ('4', 'Персональный тренер'),
        ('5', 'Тренер груповых занятий'),
        ('6', 'Тренер стажер'),
    ]

    picture = models.FileField(upload_to='trainers_photos')
    name = models.CharField(default='', null=False, max_length=50)
    position = models.CharField(max_length=1, choices=POSITION, default='4')
    description = models.TextField(max_length=400, null=False, default='')
    telephone = models.CharField(max_length=12, default='88005353535')

    def __str__(self):
        return f'{self.name}'
