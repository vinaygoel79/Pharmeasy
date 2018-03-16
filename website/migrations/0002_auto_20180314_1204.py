# Generated by Django 2.0.3 on 2018-03-14 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceId', models.IntegerField()),
                ('resourceType', models.CharField(max_length=50)),
                ('approved', models.BooleanField(default=False)),
                ('pending', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Patient')),
            ],
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='medicines',
            new_name='medicine',
        ),
    ]