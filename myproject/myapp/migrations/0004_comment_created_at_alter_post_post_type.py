# Generated by Django 4.1.3 on 2022-11-29 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_posttype_post_follow_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_tag', to=settings.AUTH_USER_MODEL),
        ),
    ]
