# Generated by Django 3.1.4 on 2021-06-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0043_auto_20210610_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Short_Part_Dept',
            field=models.CharField(default='สายงาน', max_length=10),
        ),
    ]
