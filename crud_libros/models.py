from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    """El método __str__() es una función especial en Python que se utiliza para definir
    cómo se debe representar una instancia de un objeto como una cadena de texto legible.
    """

    def __str__(self):
        return f'{self.titulo}'

    """ la clase Meta dentro de un modelo se utiliza para proporcionar metadatos adicionales sobre el modelo."""
    class Meta:
        ordering = ['-created_at']
