# Generated by Django 4.0.4 on 2022-07-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0010_alter_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='sites.tag', verbose_name='タグ'),
        ),
    ]