# Generated by Django 4.0.4 on 2022-04-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, max_length=300, upload_to='Python.svg.png'),
        ),
    ]
