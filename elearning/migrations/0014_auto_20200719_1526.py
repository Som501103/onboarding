# Generated by Django 3.0.3 on 2020-07-19 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0013_auto_20200717_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_score',
            old_name='Post_Created1',
            new_name='Post_Created',
        ),
        migrations.RenameField(
            model_name='staff_score',
            old_name='Post_Score1',
            new_name='Post_Score',
        ),
        migrations.RenameField(
            model_name='staff_score',
            old_name='Post_Created10',
            new_name='Pre_Created',
        ),
        migrations.RenameField(
            model_name='staff_score',
            old_name='Post_Score10',
            new_name='Pre_Score',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Created2',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Created3',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Created4',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Created5',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Created6',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Created7',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Created8',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Created9',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Score2',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Score3',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Score4',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Score5',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Score6',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Score7',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Score8',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Post_Score9',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created1',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created10',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created2',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created3',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created4',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created5',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created6',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created7',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created8',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Created9',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score1',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score10',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score2',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score3',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score4',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score5',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score6',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score7',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score8',
        ),
        migrations.RemoveField(
            model_name='staff_score',
            name='Pre_Score9',
        ),
        migrations.AddField(
            model_name='staff_score',
            name='Link_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Course_Score', to='elearning.Course'),
        ),
    ]
