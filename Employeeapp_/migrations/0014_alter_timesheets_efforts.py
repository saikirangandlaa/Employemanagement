# Generated by Django 3.2.16 on 2022-11-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employeeapp_', '0013_alter_timesheets_efforts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheets',
            name='efforts',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]