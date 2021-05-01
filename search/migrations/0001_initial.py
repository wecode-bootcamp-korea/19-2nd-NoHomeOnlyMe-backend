# Generated by Django 3.2 on 2021-05-01 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmenityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'amenity_types',
            },
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('road_address', models.CharField(max_length=20)),
                ('legalcode', models.CharField(max_length=20)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='search.amenitytype')),
            ],
            options={
                'db_table': 'amenities',
            },
        ),
    ]
