# Generated by Django 4.2.11 on 2024-04-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('username', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Username')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='Email')),
                ('avatar', models.ImageField(blank=True, upload_to='user/avatar', verbose_name='Avatar')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
