# Generated by Django 3.0.5 on 2021-07-24 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=120, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
