# Generated by Django 4.1.7 on 2023-05-01 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0005_comment_comment_detail_comment_commenter_post_series_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment', to='app_blog.comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='sequence',
            field=models.IntegerField(default=0),
        ),
    ]
