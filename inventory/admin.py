from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Carros, Bonecas, Jogos, Bonecos, Brindes, Outros)
class ViewAdmin(admin.ModelAdmin):
    pass