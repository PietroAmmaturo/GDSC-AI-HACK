# Generated by Django 4.2 on 2024-04-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('source_file', models.CharField(max_length=100)),
                ('related_courses', models.ManyToManyField(blank=True, to='api.course')),
            ],
        ),
    ]
