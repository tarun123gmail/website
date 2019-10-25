from django.db import models


class Human(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=500)
    full_name = models.CharField(max_length=300)
    age = models.IntegerField(default=0)
    special_note = models.CharField(max_length=5000)

    def __str__(self):
        return self.full_name


# Create your models here.
