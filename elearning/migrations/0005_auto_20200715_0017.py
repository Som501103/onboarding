# Generated by Django 3.0.3 on 2020-07-14 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0004_auto_20200714_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='Date_PostTest1',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Date_PreTest1',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Date_Vdo1_1',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Date_Vdo1_2',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Date_Vdo1_3',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Score_PostTest1',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Score_PreTest1',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Vdo_pass1_1',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Vdo_pass1_2',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Vdo_pass1_3',
        ),
        migrations.AddField(
            model_name='staff',
            name='Status',
            field=models.CharField(default='on Process', max_length=12, null=True),
        ),
        migrations.CreateModel(
            name='Staff_Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='Pre1', max_length=5)),
                ('Date_Created', models.DateTimeField(null=True)),
                ('Score', models.IntegerField(default=0, null=True)),
                ('Link_Course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Score_Courses', to='elearning.Course')),
                ('Link_SubCourse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SubCourse_Score', to='elearning.Sub_Course')),
                ('Staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Staff_score', to='elearning.Staff')),
            ],
        ),
    ]