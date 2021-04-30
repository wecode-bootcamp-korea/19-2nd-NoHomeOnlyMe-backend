# Generated by Django 3.2 on 2021-04-30 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='descriptionoption',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.home'),
        ),
        migrations.AddField(
            model_name='checkadditionaloption',
            name='additional_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.additionalinformation'),
        ),
        migrations.AddField(
            model_name='checkadditionaloption',
            name='additional_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.additionaloption'),
        ),
        migrations.AddField(
            model_name='additionalroomoption',
            name='additional_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.additionalinformation'),
        ),
        migrations.AddField(
            model_name='additionalroomoption',
            name='room_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.roomoption'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='additional_options',
            field=models.ManyToManyField(through='homes.CheckAdditionalOption', to='homes.AdditionalOption'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.home'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='maintenance_cost_options',
            field=models.ManyToManyField(through='homes.InclusionMaintenanceCost', to='homes.MaintenanceCostOption'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='room_options',
            field=models.ManyToManyField(through='homes.AdditionalRoomOption', to='homes.RoomOption'),
        ),
    ]
