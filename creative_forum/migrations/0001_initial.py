# Generated by Django 3.0.6 on 2020-06-01 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='opened', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('topic_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', related_query_name='topics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopicAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('answer_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='answers', to=settings.AUTH_USER_MODEL)),
                ('answer_for_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', related_query_name='answers', to='creative_forum.Topic')),
            ],
        ),
    ]
