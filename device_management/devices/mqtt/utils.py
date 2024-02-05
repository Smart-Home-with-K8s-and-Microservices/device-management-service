import json


def print_logs(text):
    '''Prints the provided text in bold cyan color.'''
    bold_cyan_text = f'\033[96;1m{text}\033[0m'
    print(bold_cyan_text)


def is_sensor_data_topic(mqtt_topic):
    '''Checks if the provided MQTT topic follows the 'device/+/sensor/+' pattern.'''
    topic_parts = mqtt_topic.split('/')

    return all([
        len(topic_parts) == 4,  # Check if the topic has four parts
        topic_parts[0] == 'device',  # Check if the first part is 'device'
        topic_parts[2] == 'sensor'  # Check if the third part is 'sensor'
    ])


def is_device_status_topic(mqtt_topic):
    '''Checks if the provided MQTT topic follows the 'device/+/status' pattern.'''
    topic_parts = mqtt_topic.split('/')

    return all([
        len(topic_parts) == 3,  # Check if the topic has three parts
        topic_parts[0] == 'device',  # Check if the first part is 'device'
        topic_parts[2] == 'status'  # Check if the third part is 'status'
    ])


def get_serial_from_topic(mqtt_topic):
    '''Extracts the serial number from the related MQTT topics.'''
    topic_parts = mqtt_topic.split('/')
    valid_topic = is_device_status_topic(mqtt_topic) or is_sensor_data_topic(mqtt_topic)
    return topic_parts[1] if valid_topic else None


def get_status_from_payload(mqtt_payload):
    ''' Extracts the 'status' field from the provided MQTT payload.'''
    payload = json.loads(mqtt_payload.decode())
    return payload.get('status', None)
