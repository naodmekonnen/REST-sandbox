# Generated by Django 4.1.3 on 2022-11-29 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_comment_created_at_alter_post_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='myapp.post'),
        ),
    ]
