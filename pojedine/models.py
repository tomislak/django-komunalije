from django.db import models

class Struja(models.Model):
    datum = models.DateField()
    struja = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self):
        return str(self.datum) + " " + str(self.struja)

class Plin(models.Model):
    datum = models.DateField()
    plin = models.DecimalField(max_digits=7, decimal_places=3)

    def __str__(self):
        return str(self.datum)

class Voda(models.Model):
    datum = models.DateField()
    voda = models.DecimalField(max_digits=7, decimal_places=4)

    def __str__(self):
        return str(self.datum)
