# Generated by Django 4.2.11 on 2024-07-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_historicalproject_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprojectattributetype',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalprojectattributetype',
            name='is_default_value',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='projectattributetype',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectattributetype',
            name='is_default_value',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]