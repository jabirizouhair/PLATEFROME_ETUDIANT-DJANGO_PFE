# Generated by Django 2.1.5 on 2019-02-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0012_auto_20190214_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electeur',
            name='candidat_cin',
            field=models.CharField(max_length=50, unique=1),
        ),
    ]