# Generated by Django 4.1.7 on 2023-06-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traning', '0003_alter_trainerinfo_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerinfo',
            name='telephone',
            field=models.CharField(default='88005353535', max_length=12),
        ),
    ]
