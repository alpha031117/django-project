# Generated by Django 4.1.7 on 2023-04-04 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0004_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_detail',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='series',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app_blog.series'),
        ),
        migrations.AddField(
            model_name='series',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
