# Generated by Django 5.1.1 on 2024-12-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeachRate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]