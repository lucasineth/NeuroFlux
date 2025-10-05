from django.db import models
from django.urls import reverse

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

class Tarefas(models.Model):
    frequencia_choice = (
    ('D', 'Diária'),
    ('S', 'Semanal'),
    ('M', 'Mensal'),
    ('15', '1 vez por semana'),
    ('25', '2 vez por mês'),
    ('35', '3 vez por mês'),
    ('N', 'Ao necessário'),
    ('O', 'Outro'),
    )
    tarefa = models.CharField(max_length=100)
    instrucoes = models.TextField(max_length=500)
    frequencia = models.CharField(max_length=2, choices=frequencia_choice, default="D")
    
    def __str__(self):
        return self.tarefa
    
class Consultas(models.Model):
    humor = models.IntegerField()
    registro_geral = models.TextField(max_length=500, blank=True, null=True)
    video = models.FileField(upload_to='video', blank=True, null=True)
    tarefas = models.ManyToManyField(Tarefas, blank=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Consulta de {self.paciente.nome} em {self.data_consulta}' 
    
    @property
    def link_publico(self):
        return f"http://127.0.0.1:8000{reverse('consulta_publica', kwargs={'id': self.id})}"
    
class Visualizacoes(models.Model):
    consulta = models.ForeignKey(Consultas, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()