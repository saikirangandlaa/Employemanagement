# Generated by Django 3.2.16 on 2022-11-07 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employeeapp_', '0010_timesheets_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employe',
            old_name='city',
            new_name='employeeid',
        ),
    ]
