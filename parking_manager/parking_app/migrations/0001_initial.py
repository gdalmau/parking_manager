# Generated by Django 2.2.6 on 2019-10-14 09:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=51)),
                ('phone', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('customer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='parking_app.Customer')),
                ('spot', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='parking_app.Spot')),
            ],
        ),
    ]
