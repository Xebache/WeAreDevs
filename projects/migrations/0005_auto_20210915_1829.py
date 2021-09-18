# Generated by Django 3.2.7 on 2021-09-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projects.Tag'),
        ),
    ]
