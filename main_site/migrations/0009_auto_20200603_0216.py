# Generated by Django 3.0.6 on 2020-06-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0008_auto_20200603_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='forum_nickname',
            field=models.CharField(default='user_2416551', max_length=75),
        ),
    ]
