# Generated by Django 4.2 on 2024-04-20 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_course_related_courses_course_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='questions',
            new_name='chapters',
        ),
    ]
