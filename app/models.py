from django.db import models

class Apto(models.Model):
    morador = models.CharField(max_length=255)
    condominio = models.CharField(max_length=255)
    apto = models.CharField(max_length=255)
    tel = models.CharField(max_length=16)
    email = models.EmailField()
    recebeu = models.BooleanField(default=False)  # Aceita 0 (False) ou 1 (True)
    codigo = models.CharField(max_length=50, unique=True, null=True, blank=True)  # Permite nulo ou em branco
    status = models.BooleanField(default=True)  # Aceita 1 (True) ou 0 (False)

    def __str__(self):
        return f"{self.codigo} - {self.morador}"

class Mail(models.Model):
    # Usando CharField para o nome do morador, condomínio e apartamento
    morador = models.CharField(max_length=255)
    condominio = models.CharField(max_length=255)
    apto = models.CharField(max_length=255)
    
    # Usando o campo de telefone corretamente formatado
    tel = models.CharField(max_length=16)
    
    # O campo de email permanece como EmailField
    email = models.EmailField()
    
    # O campo de status que pode ser True (1) ou False (0)
    recebeu = models.BooleanField(default=False)  # Recebeu (True ou False)
    
    # Código único para identificação da correspondência/encomenda
    codigo = models.CharField(max_length=50, unique=True, null=True, blank=True)
    
    # Definindo o tipo com um campo choices, se for possível ter valores específicos
    CORRESPONDENCIA = 1
    ENCOMENDA = 2
    TIPO_CHOICES = [
        (CORRESPONDENCIA, 'Correspondência'),
        (ENCOMENDA, 'Encomenda'),
    ]
    tipo = models.IntegerField(choices=TIPO_CHOICES)
    
    # Status de ativo ou inativo, representado por True (Ativo) ou False (Inativo)
    status = models.BooleanField(default=True)
    
    # Comando (um campo inteiro para indicar ações, pode ser melhorado conforme o contexto)
    comando = models.IntegerField()
    
    def __str__(self):
        return f"{self.codigo} - {self.morador}"
