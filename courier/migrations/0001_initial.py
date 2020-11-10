# Generated by Django 2.2 on 2020-11-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('rollNo', models.CharField(max_length=40)),
                ('Mail_Id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Company', models.CharField(max_length=50)),
                ('RollNo', models.CharField(max_length=30)),
                ('Phone', models.IntegerField(max_length=12)),
                ('OTP', models.CharField(blank=True, max_length=7)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Retrieve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OTP', models.CharField(max_length=7)),
                ('RollNo', models.CharField(max_length=30)),
            ],
        ),
    ]
