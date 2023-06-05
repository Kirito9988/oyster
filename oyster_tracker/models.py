from django.db import models


# Create your models here.
class OysterPackage(models.Model):
    received_date = models.DateField()
    harvest_date = models.DateField()
    full_name = models.CharField(max_length=100)
    note_image = models.ImageField(upload_to='notes/')  # assuming you have set up media files
