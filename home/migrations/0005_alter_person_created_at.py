# Generated by Django 4.1.6 on 2023-02-07 22:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_person_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
