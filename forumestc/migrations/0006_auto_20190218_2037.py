# Generated by Django 2.1.5 on 2019-02-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0005_remove_subject_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reponse',
            name='valider',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='valider',
            field=models.IntegerField(default=0),
        ),
    ]