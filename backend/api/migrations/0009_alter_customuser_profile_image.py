# Generated by Django 4.1.13 on 2024-03-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_images/profile.jpg', null=True, upload_to='profile_images/'),
        ),
    ]
