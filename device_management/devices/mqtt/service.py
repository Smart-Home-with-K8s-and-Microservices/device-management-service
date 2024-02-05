import devices.mqtt.utils as mqtt_utils
import paho.mqtt.client as mqtt


class MQTTService:
    '''Singleton MQTT service for managing connections, subscriptions, and message publishing.'''
    _instance = None

    def __new__(cls, broker_address, port, loop_forever=False,
                on_connect=None,  on_disconnect=None, on_message=None):

        # Create a singleton instance if not already exists
        if not cls._instance:
            cls._instance = super(MQTTService, cls).__new__(cls)
            cls._instance.client = mqtt.Client()
            cls._instance.broker_address = broker_address
            cls._instance.port = port

            # Set up callbacks
            cls._instance.client.on_connect = on_connect if on_connect else cls._instance.on_connect
            cls._instance.client.on_disconnect = on_disconnect if on_disconnect else cls._instance.on_disconnect
            cls._instance.client.on_message = on_message if on_message else cls._instance.on_message
            cls._instance.__connect(loop_forever)

        return cls._instance

    def __connect(self, loop_forever=True):
        '''Connect to the MQTT broker'''
        self.client.connect(self.broker_address, self.port, 60)

        # Start the MQTT client loop
        self.client.loop_forever() if loop_forever else self.client.loop_start()

    def disconnect(self):
        '''Disconnect from the MQTT broker'''
        self.client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        '''Default callback when connected to MQTT broker'''
        mqtt_utils.print_logs(f'MQTT: Connected with result code {str(rc)}')

    def on_disconnect(self, client, userdata, rc):
        '''Default callback when disconnected from the MQTT broker'''
        if rc != 0:
            mqtt_utils.print_logs(f'Disconnected with result code {rc}.')

    def on_message(self, client, userdata, msg):
        '''Default callback when a message is received'''
        mqtt_utils.print_logs(
            f'MQTT: Received message: "{msg.payload.decode()}" on topic {msg.topic}')

    def publish(self, topic, message):
        '''Publish a message to the specified topic'''
        self.client.publish(topic, message)
