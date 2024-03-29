# Generated by Django 3.2.23 on 2024-02-04 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(max_length=255)),
                ('fqbn', models.CharField(max_length=255)),
                ('sketch_name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('connected', 'Connected'), ('disconnected', 'Disconnected'), ('not_set_up', 'Not Set Up')], default='not_set_up', max_length=20)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='devices.room')),
            ],
        ),
    ]
