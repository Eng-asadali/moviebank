from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    imgPath = models.ImageField()
    duration = models.IntegerField()
    language = models.CharField(max_length=30)
    userRating = models.CharField(max_length=30)

    class Meta:
        db_table = "movies"

    def __str__(self):
        return self.name
