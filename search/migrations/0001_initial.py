# Generated by Django 3.2 on 2021-07-12 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
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
                ('regal_address', models.CharField(max_length=500, null=True)),
                ('road_address', models.CharField(max_length=500)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('amenity_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='search.amenitytype')),
                ('dong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='amenity', to='rooms.dong')),
                ('gu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='amenity', to='rooms.gu')),
            ],
            options={
                'db_table': 'amenities',
            },
        ),
    ]
