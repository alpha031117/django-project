# Generated by Django 4.1.7 on 2023-05-11 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0020_remove_post_upload_postfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_blog.post'),
        ),
        migrations.AlterField(
            model_name='replycomment',
            name='reply_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_blog.comment'),
        ),
    ]
