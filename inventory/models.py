from django.db import models

# Create your models here.

class Brinquedos(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField()
    choices = (
        ("DISPONÍVEL", "O item está disponível para compra"),
        ("ESGOTADO", "Todos os itens foram vendidos"),
        ("RESTOCKING", "Novos itens com a especificação chegarão em breve")
    )
    status = models.CharField(max_length=200, choices=choices, default="RESTOCKING") #ESGOTADO, DISPONÍVEL, RESTOCKING
    issues = models.CharField(max_length=200, default="OK")

    def __str__(self):
        return 'Nome: {0} Preço: {1}'.format(self.nome, self.price)

    class Meta:
        abstract = True

class Carros(Brinquedos):
    pass

class Bonecas(Brinquedos):
    pass

class Jogos(Brinquedos):
    pass

class Bonecos(Brinquedos):
    pass

class Brindes(Brinquedos):
    pass

class Outros(Brinquedos):
    pass