from django.db import models

class Pacientes(models.Model):
    queixa_choice = (
        ('Déficit de atenção', 'Déficit de atenção'),
        ('Hiperatividade', 'Hiperatividade'),
        ('Impulsividade', 'Impulsividade'),
        ('Ansiedade', 'Ansiedade'),
        ('Depressão', 'Depressão'),
        ('Cefaleia', 'Cefaleia'),
        ('Tontura', 'Tontura'),
        ('Convulsão', 'Convulsão'),
        ('Perda de consciência', 'Perda de consciência'),
        ('Fraqueza muscular', 'Fraqueza muscular'),
        ('Dormência ou formigamento', 'Dormência ou formigamento'),
        ('Problemas de memória', 'Problemas de memória'),
        ('Alterações de humor', 'Alterações de humor'),
        ('Dificuldade de concentração', 'Dificuldade de concentração'),
        ('Distúrbios do sono', 'Distúrbios do sono'),
        ('Outro', 'Outro'),
    )
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    pagamento_em_dia = models.BooleanField(default=True)
    queixa = models.TextField(max_length=500, choices=queixa_choice)

    def __str__(self):
        return self.nome

