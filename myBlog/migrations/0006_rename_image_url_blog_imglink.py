# Generated by Django 3.2.6 on 2022-03-26 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0005_alter_blog_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Image_URL',
            new_name='ImgLink',
        ),
    ]
