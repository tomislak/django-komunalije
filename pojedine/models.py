from django.db import models

class Pojedine(models.Model):
    datum = models.DateField()
    struja = models.DecimalField(max_digits=7, decimal_places=1)
    plin = models.DecimalField(max_digits=7, decimal_places=3)
    voda = models.DecimalField(max_digits=7, decimal_places=4)

    def __str__(self):
        return str(self.datum)
