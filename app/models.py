from django.db import models


class mymodel(models.Model):
    image = models.ImageField(upload_to='images/')


    




