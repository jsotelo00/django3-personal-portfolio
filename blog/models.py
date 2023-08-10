from django.db import models

class Blog(models.Model):
    tittle = models.CharField(max_length=200)
    date = models.DateField()
    descritption = models.TextField()

    def __str__(self):
        return self.tittle
