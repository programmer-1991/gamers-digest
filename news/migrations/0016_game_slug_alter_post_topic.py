# Generated by Django 4.2.10 on 2024-04-15 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_alter_post_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.game'),
        ),
    ]