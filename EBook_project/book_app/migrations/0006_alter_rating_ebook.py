# Generated by Django 3.2 on 2022-11-26 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0005_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='ebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='book_app.ebook'),
        ),
    ]