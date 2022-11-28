from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Genre(models.Model):
    category=models.CharField(max_length=250)

    def __str__(self):
        return self.category

class Ebook(models.Model):
    title=models.CharField(max_length=500)
    author=models.CharField(max_length=250)
    category=models.ForeignKey(Genre,on_delete=models.CASCADE,related_name='ebook')
    createdby=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return  self.title

#
class Rating(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    ebook=models.ForeignKey(Ebook,on_delete=models.CASCADE,related_name='rating')
    favourite=models.BooleanField(default=False)

    def __str__(self):
        return str(self.rating)+" "+self.ebook.title
