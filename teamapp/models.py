from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=100)
    nombre_tecnico = models.CharField(max_length=40)
    gerente = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logosequipo',default = 'logosequipo/default.png', null=True, blank=True)

    def __str__(self):
        return self.nombre

    def obtener_logo(self):
        if self.logo:
            return mark_safe('<img src="{0}" width="100" height="110" alt="Foto"/>'.format(self.logo.url)) 
        else:
            return mark_safe('<img src="default.png" width="120" height="100" alt="Usuario sin foto"/>')

class Jugador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotosjugadores',default = 'fotosjugadores/default.png', null=True, blank=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    peso = models.FloatField()
    estatura = models.FloatField()

    def __str__(self):
        return self.nombre

    def obtener_foto(self):
        if self.foto:
            return mark_safe('<img src="{0}" width="100" height="110" alt="Foto">'.format(self.foto.url)) 
        else:
            return mark_safe('<img src="default.png" width="120" height="100" alt="Usuario sin foto"/>')





