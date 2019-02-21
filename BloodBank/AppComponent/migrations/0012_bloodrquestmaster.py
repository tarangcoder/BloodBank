# Generated by Django 2.1.5 on 2019-02-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppComponent', '0011_auto_20190209_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRquestMaster',
            fields=[
                ('PkId', models.AutoField(primary_key=True, serialize=False)),
                ('BloodType', models.CharField(max_length=20)),
                ('Gender', models.TextField()),
                ('Quantity', models.TextField()),
                ('DeliverDate', models.TextField()),
                ('UserId', models.TextField()),
                ('CreatedOn', models.CharField(max_length=20)),
                ('CreatedBy', models.CharField(max_length=20)),
                ('ModifiedOn', models.CharField(max_length=20)),
                ('ModifiedBy', models.CharField(max_length=20)),
                ('isActive', models.BooleanField()),
            ],
            options={
                'db_table': 'tbl_BloodReqMaster',
            },
        ),
    ]
