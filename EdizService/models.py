from django.db import models

class Service(models.Model):
    servis_adi = models.CharField(max_length=80)
    servis_tip = models.CharField(max_length=2)
    servis_aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.servis_adi
# Create your models here.
