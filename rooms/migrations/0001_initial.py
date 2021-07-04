# Generated by Django 3.2 on 2021-07-02 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_cost', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('parking_fee', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('is_agreement', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'additional_informations',
            },
        ),
        migrations.CreateModel(
            name='AdditionalOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'additional_options',
            },
        ),
        migrations.CreateModel(
            name='BuildingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'building_types',
            },
        ),
        migrations.CreateModel(
            name='Dong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
            options={
                'db_table': 'dong',
            },
        ),
        migrations.CreateModel(
            name='Gu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
            options={
                'db_table': 'gu',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceCostOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'maintenance_cost_options',
            },
        ),
        migrations.CreateModel(
            name='MoveInOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'move_in_options',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('road_address', models.CharField(max_length=500)),
                ('regal_address', models.CharField(max_length=500, null=True)),
                ('apt_dong', models.CharField(max_length=20, null=True)),
                ('apt_ho', models.CharField(max_length=20, null=True)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('building_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.buildingtype')),
                ('dong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.dong')),
                ('gu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.gu')),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'room_options',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'room_types',
            },
        ),
        migrations.CreateModel(
            name='SaleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sale_type',
            },
        ),
        migrations.CreateModel(
            name='SaleInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=18)),
                ('monthly_pay', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('is_short', models.BooleanField(default=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_info', to='rooms.room')),
                ('sale_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.saletype')),
            ],
            options={
                'db_table': 'sale_informations',
            },
        ),
        migrations.CreateModel(
            name='RoomInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_pyeong', models.IntegerField()),
                ('supply_m2', models.DecimalField(decimal_places=5, max_digits=15)),
                ('exclusive_pyeong', models.IntegerField()),
                ('exclusive_m2', models.DecimalField(decimal_places=5, max_digits=15)),
                ('building_story', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('heating_type', models.CharField(max_length=50)),
                ('move_in_date', models.DateField(null=True)),
                ('move_in_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.moveinoption')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_info', to='rooms.room')),
            ],
            options={
                'db_table': 'room_informations',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.roomtype'),
        ),
        migrations.CreateModel(
            name='InclusionMaintenanceCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.additionalinformation')),
                ('maintenance_cost_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.maintenancecostoption')),
            ],
            options={
                'db_table': 'inclusion_maintenance_cost',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('sequence', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rooms.room')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='dong',
            name='gu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.gu'),
        ),
        migrations.CreateModel(
            name='DescriptionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('secret_text', models.TextField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
            ],
            options={
                'db_table': 'description_options',
            },
        ),
        migrations.CreateModel(
            name='CheckAdditionalOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_able', models.BooleanField(default=False)),
                ('additional_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.additionalinformation')),
                ('additional_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.additionaloption')),
            ],
            options={
                'db_table': 'check_additional_options',
            },
        ),
        migrations.CreateModel(
            name='AdditionalRoomOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.additionalinformation')),
                ('room_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomoption')),
            ],
            options={
                'db_table': 'additional_room_options',
            },
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='additional_options',
            field=models.ManyToManyField(through='rooms.CheckAdditionalOption', to='rooms.AdditionalOption'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='maintenance_cost_options',
            field=models.ManyToManyField(through='rooms.InclusionMaintenanceCost', to='rooms.MaintenanceCostOption'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='room_options',
            field=models.ManyToManyField(through='rooms.AdditionalRoomOption', to='rooms.RoomOption'),
        ),
    ]
