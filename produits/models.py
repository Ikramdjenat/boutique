from django.db import models

class Product(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='produits/', null=True, blank=True)

    def __str__(self):
        return self.nom
