# Generated by Django 3.2.7 on 2022-01-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=150)),
                ('did', models.CharField(max_length=150)),
                ('rate', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='d_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=150)),
                ('medicine', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('rate', models.CharField(max_length=150)),
                ('cardno', models.CharField(max_length=150)),
                ('cardname', models.CharField(max_length=150)),
                ('cardmonth', models.CharField(max_length=150)),
                ('cardyear', models.CharField(max_length=150)),
                ('cv', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='l_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=150)),
                ('medicine', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('rate', models.CharField(max_length=150)),
                ('cardno', models.CharField(max_length=150)),
                ('cardname', models.CharField(max_length=150)),
                ('cardmonth', models.CharField(max_length=150)),
                ('cardyear', models.CharField(max_length=150)),
                ('cv', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='medical_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_illness', models.CharField(max_length=150)),
                ('test_report', models.CharField(max_length=150)),
                ('height', models.CharField(max_length=150)),
                ('weight', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('bloodgrp', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('pid', models.CharField(max_length=150)),
                ('file', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=150)),
                ('medicine', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('rate', models.CharField(max_length=150)),
                ('cardno', models.CharField(max_length=150)),
                ('cardname', models.CharField(max_length=150)),
                ('cardmonth', models.CharField(max_length=150)),
                ('cardyear', models.CharField(max_length=150)),
                ('cv', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='pregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('pincode', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=150)),
                ('diseases', models.CharField(max_length=150)),
                ('medicine', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('pharmacy', models.CharField(max_length=150)),
                ('lab', models.CharField(max_length=150)),
                ('pid', models.CharField(max_length=150)),
            ],
        ),
    ]
