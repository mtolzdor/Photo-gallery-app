from django.db import models

class Photos(models.Model):
    photo = models.ImageField(upload_to = 'images')

def _str_(self):
    return self.photo
