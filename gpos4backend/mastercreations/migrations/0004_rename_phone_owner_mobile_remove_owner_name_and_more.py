# Generated by Django 5.1.5 on 2025-02-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastercreations', '0003_employeemaster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='phone',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='name',
        ),
        migrations.AddField(
            model_name='owner',
            name='firstname',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='lastname',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
