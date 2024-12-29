from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2, max_digits=12)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=20)
    cost = models.DecimalField(decimal_places=2, max_digits=12)
    size = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

