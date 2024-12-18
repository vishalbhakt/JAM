# Generated by Django 4.1 on 2022-08-30 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0003_remove_employer_id_alter_employer_cpemailaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=50)),
                ('enquirytext', models.TextField()),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
    ]
