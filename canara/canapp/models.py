from django.db import models
import os

def update_filename1(instance, filename):
    extension = os.path.splitext(filename)[1]
    path = instance.branch_name
    format = 'front_view' + extension
    return os.path.join(path, format)

def update_filename2(instance, filename):
    extension = os.path.splitext(filename)[1]
    path = instance.branch_name
    format = 'back_view' + extension
    return os.path.join(path, format)

def update_filename3(instance, filename):
    extension = os.path.splitext(filename)[1]
    path = instance.branch_name
    format = 'top_view' + extension
    return os.path.join(path, format)


# Create your models here.
class Atm(models.Model):
    branch_name = models.CharField(max_length=250)
    branch_code = models.CharField(max_length=250)
    # atm_img = models.ImageField(upload_to='atms')
    front_view = models.FileField(upload_to=update_filename1)
    back_view = models.FileField(upload_to=update_filename2)
    top_view = models.FileField(upload_to=update_filename3)

    def __str__(self):
        return self.name
