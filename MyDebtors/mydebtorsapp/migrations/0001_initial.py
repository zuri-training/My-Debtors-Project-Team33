# Generated by Django 4.0 on 2022-07-29 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_admin', models.CharField(max_length=100)),
                ('school_email', models.EmailField(max_length=254)),
                ('school_address', models.CharField(max_length=100)),
                ('school_location', models.CharField(max_length=100)),
                ('school_phone_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_email', models.EmailField(max_length=100)),
                ('parent_phone_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(default='XYZ', max_length=100)),
                ('admission_no', models.CharField(max_length=12)),
                ('fees_owed', models.IntegerField()),
                ('last_school', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='mydebtorsapp.school')),
            ],
        ),
    ]
