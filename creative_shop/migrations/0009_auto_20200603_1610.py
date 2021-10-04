# Generated by Django 3.0.6 on 2020-06-03 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creative_shop', '0008_auto_20200603_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
