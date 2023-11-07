from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    nombre=models.CharField(max_length=50)
    documento=models.IntegerField()    
    ficha=models.IntegerField()
    photo=models.ImageField(upload_to='fotos_aprendices')

    def __str__(self):
        return self.nombre