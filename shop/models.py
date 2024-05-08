from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fruit'
        verbose_name = 'fruit'
        verbose_name_plural = 'fruits'
