# Generated by Django 4.1.2 on 2022-12-04 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_designation_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='designation',
        ),
    ]
