# Generated by Django 4.1.7 on 2023-05-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0018_remove_post_upload_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
