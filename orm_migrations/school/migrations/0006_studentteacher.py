# Generated by Django 4.2.14 on 2024-09-13 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_rename_teacher_student_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher_set', to='school.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher_set', to='school.teacher')),
            ],
        ),
    ]
