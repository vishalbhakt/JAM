# Generated by Django 4.1 on 2022-08-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('dob', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=20)),
                ('keyskills', models.TextField()),
                ('regdate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('usertype', models.CharField(max_length=50)),
            ],
        ),
    ]
