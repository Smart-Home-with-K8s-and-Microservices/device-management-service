# yourapp/management/commands/populate_data.py

import json
import os
from django.core.management.base import BaseCommand
from devices.models import Device, Sensor
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with device data'

    def handle(self, *args, **options):
        self.stdout.write('Populating the database...')

        # Check if the configurations file exists
        config_file_path = 'devices.json'
        if not os.path.exists(config_file_path):
            self.stdout.write(self.style.ERROR(f'Devices file "{config_file_path}" not found.'))
            return

        # Load device and sensor configurations from a JSON file
        with open(config_file_path, 'r') as config_file:
            configurations = json.load(config_file)

        # Loop through each configuration
        for config in configurations:
            # Check if the Device with the given serial already exists
            device, created = Device.objects.get_or_create(**config['device'])

            # If the Device was just created, create sensors for it
            if created:
                for sensor_info in config['sensors']:
                    sensor = Sensor.objects.create(device=device, **sensor_info)

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
