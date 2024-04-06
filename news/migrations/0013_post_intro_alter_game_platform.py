# Generated by Django 4.2.10 on 2024-03-29 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_game_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.IntegerField(choices=[(0, ''), (1, 'Xbox'), (2, 'Playstation'), (3, 'Nintendo'), (4, 'Windows')], default=0),
        ),
    ]