# Generated by Django 2.1.5 on 2019-02-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppComponent', '0010_auto_20190207_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='EmailId',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
