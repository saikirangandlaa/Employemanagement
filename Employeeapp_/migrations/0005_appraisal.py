# Generated by Django 3.2.16 on 2022-11-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employeeapp_', '0004_auto_20221105_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance', models.CharField(max_length=35)),
                ('salary', models.CharField(max_length=35)),
                ('progress', models.CharField(max_length=35)),
                ('feedback', models.CharField(max_length=35)),
                ('hikegot', models.CharField(max_length=35)),
            ],
        ),
    ]