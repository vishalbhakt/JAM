# Generated by Django 4.1 on 2022-08-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0002_employer_alter_jobseeker_emailaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='id',
        ),
        migrations.AlterField(
            model_name='employer',
            name='cpemailaddress',
            field=models.EmailField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
