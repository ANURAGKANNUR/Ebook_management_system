from django.contrib import admin
from .models import Genre,Ebook,Rating
# Register your models here.
admin.site.register(Genre)
admin.site.register(Ebook)
admin.site.register(Rating)