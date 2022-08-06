# Generated by Django 4.0.5 on 2022-07-02 13:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('text', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('link', models.CharField(blank=True, max_length=2000, null=True, verbose_name='リンク')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]