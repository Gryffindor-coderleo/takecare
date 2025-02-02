# Generated by Django 3.2.7 on 2022-01-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='labbill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=150)),
                ('medicine', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('rate', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='labreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('place', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phno', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='labtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=150)),
                ('count', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='labtestcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='testreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(max_length=150)),
                ('height', models.CharField(max_length=150)),
                ('weight', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('test1', models.CharField(max_length=150)),
                ('test2', models.CharField(max_length=150)),
                ('test3', models.CharField(max_length=150)),
                ('other', models.CharField(max_length=150)),
            ],
        ),
    ]
