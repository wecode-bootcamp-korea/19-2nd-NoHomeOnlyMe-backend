# Generated by Django 3.2 on 2021-07-12 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=1000, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('kakao_code', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'db_table': 'users',
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.ManyToManyField(related_name='user_likes', through='users.Like', to='rooms.Room'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
