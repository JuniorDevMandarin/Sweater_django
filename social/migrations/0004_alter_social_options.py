# Generated by Django 4.0.5 on 2022-08-31 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_social_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'ordering': ['-id'], 'verbose_name': 'Post', 'verbose_name_plural': 'Post'},
        ),
    ]
