# Generated by Django 3.1.6 on 2021-02-17 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_number', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='possession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carOwner_possession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
                ('car_possession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
            ],
        ),
        migrations.CreateModel(
            name='driverID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_number', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('carOwner_driverID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
    ]
