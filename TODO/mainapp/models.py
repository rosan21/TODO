from django.db import models

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=25)
    desc = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    First_name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.First_name
