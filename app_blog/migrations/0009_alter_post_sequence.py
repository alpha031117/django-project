# Generated by Django 4.1.7 on 2023-05-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0008_alter_post_options_post_created_on_post_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sequence',
            field=models.IntegerField(default=1),
        ),
    ]