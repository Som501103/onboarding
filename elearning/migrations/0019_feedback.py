# Generated by Django 3.0.3 on 2020-07-20 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0018_course_cover_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300)),
                ('Detail', models.TextField(blank=True, default='detail', null=True)),
                ('Date_Created', models.DateTimeField(null=True)),
                ('Staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Staff_feedback', to='elearning.Staff')),
            ],
        ),
    ]