# Generated by Django 3.0.5 on 2020-05-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroPersona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='representante',
            field=models.CharField(default='S', max_length=1),
            preserve_default=False,
        ),
    ]