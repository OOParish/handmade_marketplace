# Generated by Django 3.0.6 on 2020-06-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0016_auto_20200603_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='forum_nickname',
            field=models.CharField(default='user_3274177', max_length=75),
        ),
    ]
