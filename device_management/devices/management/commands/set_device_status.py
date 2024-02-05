import os

import devices.mqtt.utils as mqtt_utils
from devices.mqtt.service import MQTTService
from devices.services import update_device_status
from django.core.management.base import BaseCommand

DEVICES_TOPIC = 'device/+/status'


def on_message(client, userdata, msg):
    mqtt_utils.print_logs(
        f'MQTT Client from Django Command "set_device_status": Incoming message => "{msg.payload.decode()}" on topic {msg.topic}')

    try:
        device_serial = mqtt_utils.get_serial_from_topic(msg.topic)

        if device_serial:
            device_status = mqtt_utils.get_status_from_payload(msg.payload)
            update_device_status(device_serial, device_status)
    
    except Exception as e:
        mqtt_utils.print_logs(f'Error processing MQTT message: {e}')
        return


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        mqtt_utils.print_logs(f'MQTT: Connected with result code {str(rc)}')
        client.subscribe(DEVICES_TOPIC)
    else:
        mqtt_utils.print_logs("Bad connection Returned code=", rc)


class Command(BaseCommand):
    help = 'Starts the MQTT listener'

    def handle(self, *args, **options):

        # Set up your MQTT broker connection
        broker_address = os.getenv('MQTT_BROKER')
        port = int(os.getenv('MQTT_PORT'))

        MQTTService(broker_address, port,
                    on_connect=on_connect,
                    on_message=on_message,
                    loop_forever=True)
