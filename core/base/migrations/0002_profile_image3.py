# Generated by Django 5.0.4 on 2024-05-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='profiles3/'),
        ),
    ]
