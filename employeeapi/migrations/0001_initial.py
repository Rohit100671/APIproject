# Generated by Django 5.1.2 on 2024-11-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAPI',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'Employeeapi',
            },
        ),
    ]
