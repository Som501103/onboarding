# Generated by Django 3.1.4 on 2021-06-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0045_auto_20210614_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='StaffPosition',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
