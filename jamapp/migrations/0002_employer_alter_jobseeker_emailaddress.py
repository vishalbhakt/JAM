# Generated by Django 4.1 on 2022-08-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firmname', models.CharField(max_length=100)),
                ('firmwork', models.TextField()),
                ('firmaddress', models.TextField()),
                ('cpname', models.CharField(max_length=50)),
                ('cpcontactno', models.CharField(max_length=15)),
                ('cpemailaddress', models.EmailField(max_length=12)),
                ('aadharno', models.CharField(max_length=12)),
                ('panno', models.CharField(max_length=10)),
                ('gstno', models.CharField(max_length=15)),
                ('regdate', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='emailaddress',
            field=models.EmailField(max_length=50, primary_key='True', serialize=False),
        ),
    ]
