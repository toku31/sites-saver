# Generated by Django 4.0.4 on 2022-07-16 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_site_user_alter_site_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='登録日'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='登録日'),
            preserve_default=False,
        ),
    ]
