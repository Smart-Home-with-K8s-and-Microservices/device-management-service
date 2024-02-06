import devices.mqtt.utils as mqtt_utils
from devices.mqtt.service import MQTTService
from django.conf import settings


def update_device_status(device_serial, device_status):
    '''Update the status of a device in the database.'''

    from devices.models import Device

    try:
        # Retrieve the corresponding device from the database
        device = Device.objects.get(serial=device_serial)
    except Device.DoesNotExist:
        print(f'Device with serial "{device_serial}" does not exist.')
        return

    # Update the device status based on the provided status
    if device_status == 'online':
        device.status = 'connected'
    elif device_status == 'offline':
        device.status = 'disconnected'

    # Save the changes
    device.save()


def send_command_to_sensor(device_serial, sensor_serial, command):
    '''Send a command to a sensor via MQTT.'''

    # get or create the mqtt service
    mqtt_service = MQTTService(
        broker_address=settings.MQTT_BROKER,
        port=int(settings.MQTT_PORT))

    # construct command topic
    topic = mqtt_utils.get_command_topic(device_serial, sensor_serial)

    # send command
    mqtt_service.publish(topic, command)
