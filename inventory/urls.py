from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display_bonecas', views.display_bonecas, name="display_bonecas"),
    path('display_bonecos', views.display_bonecos, name="display_bonecos"),
    path('display_carros', views.display_carros, name="display_carros"),
    path('display_jogos', views.display_jogos, name="display_jogos"),
    path('display_brindes', views.display_brindes, name="display_brindes"),
    path('display_outros', views.display_outros, name="display_outros"),
    path('add_boneca', views.add_boneca, name="add_boneca"),
    path('add_boneco', views.add_boneco, name="add_boneco"),
    path('add_carro', views.add_carro, name="add_carro"),
    path('add_jogo', views.add_jogo, name="add_jogo"),
    path('add_brinde', views.add_brinde, name="add_brinde"),
    path('add_outro', views.add_outro, name="add_outro"),
    path('edit_boneca/<int:pk>/', views.edit_boneca, name="edit_boneca"),

]