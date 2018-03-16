# Generated by Django 2.0.3 on 2018-03-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20180314_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='pharmacist',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]