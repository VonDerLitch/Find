from django.db import models
from django.contrib.auth.models import User

class Profissional(models.Model):
    AREA_CHOICES = [
        ('faxineira', 'Faxineira'),
        ('pintor', 'Pintor'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    area = models.CharField(max_length=100, choices=AREA_CHOICES)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50, default='Brasileiro (a)')