from django.contrib.auth.models import User
from django.db import models
from traning.models import TrainerInfo


# Create your models here.
class TrainRegModel(models.Model):
    time_choices = [(str(i) + ':00', str(i) + ':00') for i in range(8, 23)]
    time_slot = models.CharField(max_length=5, choices=time_choices)
    is_booked = models.BooleanField(default=False)
    trainer = models.ForeignKey(TrainerInfo, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.time_slot
