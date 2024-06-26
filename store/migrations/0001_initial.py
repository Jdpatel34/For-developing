# Generated by Django 5.0.6 on 2024-05-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('mobile_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('country', models.CharField(default='United Kindom', max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('postcode', models.CharField(max_length=10)),
            ],
        ),
    ]
