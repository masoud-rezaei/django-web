# Generated by Django 4.0.3 on 2022-03-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'can read all books')]},
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, upload_to='covers/'),
        ),
    ]
