#  produits
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('produit/<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('produit/<int:produit_id>/ajouter/', views.ajouter_au_panier, name='ajouter_au_panier'),
path('panier/', views.afficher_panier, name='afficher_panier'),
path('panier/supprimer/<int:produit_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),

]
