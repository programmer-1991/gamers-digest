# Generated by Django 4.2.10 on 2024-03-12 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_updated_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='exerpt',
            new_name='excerpt',
        ),
    ]
