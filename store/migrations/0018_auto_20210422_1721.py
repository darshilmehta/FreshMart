# Generated by Django 3.1.7 on 2021-04-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_feedback_feedback_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback_image',
            field=models.FileField(default='no_img.png', upload_to='feedback_images'),
        ),
    ]
