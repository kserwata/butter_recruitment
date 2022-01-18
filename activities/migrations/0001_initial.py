# Generated by Django 4.0.1 on 2022-01-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('activity_date', models.DateTimeField()),
                ('track_id', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('R', 'R')], max_length=1)),
                ('billing_amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
