# Generated by Django 5.0.6 on 2024-06-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
