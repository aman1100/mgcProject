# Generated by Django 3.1.4 on 2021-05-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('nameOfApplicant', models.CharField(default='', max_length=50)),
                ('fatherName', models.CharField(default='', max_length=50)),
                ('motherName', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('zip', models.CharField(default='', max_length=50)),
                ('aadhar', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pan', models.CharField(default='', max_length=50)),
                ('officeName', models.CharField(default='', max_length=50)),
                ('officeAddress', models.CharField(default='', max_length=50)),
                ('designation', models.CharField(default='', max_length=50)),
                ('bossName', models.CharField(default='', max_length=50)),
                ('experience', models.CharField(default='', max_length=50)),
                ('refName', models.CharField(default='', max_length=50)),
                ('refContactnum', models.CharField(default='', max_length=50)),
                ('refRelationship', models.CharField(default='', max_length=50)),
                ('refAddress', models.CharField(default='', max_length=50)),
            ],
        ),
    ]