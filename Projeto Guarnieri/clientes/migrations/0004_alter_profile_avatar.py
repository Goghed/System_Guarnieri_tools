# Generated by Django 5.1.6 on 2025-02-12 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='images/avatars/default-avatar.jpg', null=True, upload_to='avatars/'),
        ),
    ]
