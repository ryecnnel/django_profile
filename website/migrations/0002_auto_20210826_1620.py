# Generated by Django 3.2.6 on 2021-08-26 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
