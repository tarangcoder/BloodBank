# Generated by Django 2.1.5 on 2019-01-31 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('AdminId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('CreatedBy', models.CharField(max_length=20)),
                ('CreatedOn', models.CharField(max_length=20)),
                ('ModifiedBy', models.CharField(max_length=20)),
                ('ModifiedOn', models.CharField(max_length=20)),
                ('isActive', models.BooleanField()),
            ],
            options={
                'db_table': 'tbl_Admin',
            },
        ),
        migrations.CreateModel(
            name='BloodSmpReports',
            fields=[
                ('RepId', models.AutoField(primary_key=True, serialize=False)),
                ('SeqNo', models.BigIntegerField()),
                ('BldTrnType', models.CharField(max_length=20)),
                ('APostiveCnt', models.BigIntegerField()),
                ('ANegativeCnt', models.BigIntegerField()),
                ('BPositiveCnt', models.BigIntegerField()),
                ('BNegativeCnt', models.BigIntegerField()),
                ('ABPositiveCnt', models.BigIntegerField()),
                ('ABNegativeCnt', models.BigIntegerField()),
                ('OPositiveCnt', models.BigIntegerField()),
                ('ONegativeCnt', models.BigIntegerField()),
                ('CreatedBy', models.CharField(max_length=20)),
                ('CreatedOn', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tbl_BloodReports',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('ContactId', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=50)),
                ('EmailId', models.EmailField(max_length=254)),
                ('ContactNo', models.BigIntegerField()),
                ('Message', models.CharField(max_length=250)),
                ('CreatedBy', models.CharField(max_length=20)),
                ('CreatedOn', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tbl_ContactDetail',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('ContactPkId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('ContactNo', models.BigIntegerField()),
                ('Comments', models.CharField(max_length=250)),
                ('Suggestion', models.CharField(max_length=250)),
                ('PostedOn', models.CharField(max_length=20)),
                ('isActive', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'tbl_contactUs',
            },
        ),
        migrations.CreateModel(
            name='DonorRegistration',
            fields=[
                ('DnrRegId', models.AutoField(primary_key=True, serialize=False)),
                ('DonorRegNumber', models.CharField(max_length=50)),
                ('FullName', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50, null=True)),
                ('Gender', models.CharField(max_length=50)),
                ('Age', models.CharField(max_length=50, null=True)),
                ('DOB', models.CharField(max_length=50, null=True)),
                ('BloodGroup', models.CharField(max_length=50)),
                ('LastDonated', models.CharField(max_length=50, null=True)),
                ('ContactNo', models.BigIntegerField(null=True)),
                ('State', models.CharField(max_length=50, null=True)),
                ('City', models.CharField(max_length=50, null=True)),
                ('Country', models.CharField(max_length=50, null=True)),
                ('EmailId', models.EmailField(max_length=254, null=True)),
                ('Weight', models.BigIntegerField(null=True)),
                ('CreatedBy', models.CharField(max_length=20)),
                ('CreatedOn', models.CharField(max_length=20)),
                ('ModifiedBy', models.CharField(max_length=20)),
                ('ModifiedOn', models.CharField(max_length=20)),
                ('isActive', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'tbl_DonorList',
            },
        ),
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('LoginHistoryId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.CharField(max_length=20)),
                ('LoggedOn', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tbl_loginHistory',
            },
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('LogUserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('CreatedBy', models.CharField(max_length=20)),
                ('CreatedOn', models.CharField(max_length=20)),
                ('ModifiedBy', models.CharField(max_length=20)),
                ('ModifiedOn', models.CharField(max_length=20)),
                ('isActive', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'tbl_UserLogin',
            },
        ),
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('RegUserId', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(default='', max_length=50)),
                ('Gender', models.CharField(default='', max_length=8)),
                ('Address', models.CharField(default='', max_length=100)),
                ('BloodGroup', models.CharField(default='', max_length=10)),
                ('MobileNo', models.BigIntegerField(default=0)),
                ('Country', models.CharField(default='', max_length=20)),
                ('State', models.CharField(default='', max_length=20)),
                ('City', models.CharField(default='', max_length=20)),
                ('PinCode', models.BigIntegerField(default=0)),
                ('PersonInfo', models.CharField(default='', max_length=250)),
                ('EmailId', models.EmailField(default='', max_length=254)),
                ('UserID', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'tbl_UserRegistration',
            },
        ),
        migrations.CreateModel(
            name='StockDetail',
            fields=[
                ('StockId', models.AutoField(primary_key=True, serialize=False)),
                ('Sample', models.CharField(max_length=50)),
                ('Quantity', models.BigIntegerField()),
                ('PurchasedOn', models.CharField(max_length=20)),
                ('ExpireOn', models.CharField(max_length=20)),
                ('CreatedBy', models.CharField(max_length=20)),
                ('CreatedOn', models.CharField(max_length=20)),
                ('ModifiedBy', models.CharField(max_length=20)),
                ('ModifiedOn', models.CharField(max_length=20)),
                ('isActive', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'tbl_StockDetail',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='UsersImage',
            fields=[
                ('ImageId', models.AutoField(primary_key=True, serialize=False)),
                ('ImageName', models.CharField(max_length=20)),
                ('ImageBase64String', models.TextField(max_length=20)),
                ('ImageType', models.CharField(max_length=20)),
                ('UpdatedOn', models.CharField(max_length=20)),
                ('UserId', models.BigIntegerField()),
            ],
            options={
                'db_table': 'tbl_UersImage',
            },
        ),
    ]
