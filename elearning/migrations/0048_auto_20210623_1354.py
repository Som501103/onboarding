# Generated by Django 3.0.7 on 2021-06-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0047_auto_20210614_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtual_class',
            name='Link_zoom',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='virtual_class',
            name='meeting_id',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
