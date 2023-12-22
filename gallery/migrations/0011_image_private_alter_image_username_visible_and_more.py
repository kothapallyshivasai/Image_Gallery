# Generated by Django 5.0 on 2023-12-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_deleted_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='username_visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
