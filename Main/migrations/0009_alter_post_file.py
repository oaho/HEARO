# Generated by Django 4.2 on 2023-06-15 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0008_alter_post_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="file",
            field=models.FileField(upload_to=""),
        ),
    ]
