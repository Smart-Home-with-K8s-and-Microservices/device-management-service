import json
import subprocess

from .exceptions import DeviceUnknownResponseException


def compile_and_flash_device(ssid, password, ip, fqbn, sketch):
    '''Compile and flash an Arduino device with the provided parameters.'''
    
    # Compilation command for arduino-cli
    compilation_command = [
        'arduino-cli',
        'compile',
        '--build-property',
        f'build.extra_flags="-DWIFI_SSID="{ssid}"" -DWIFI_PASSWORD="{password}""" -DSERVER_IP="{ip}"""',
        '--fqbn',
        f'{fqbn}',
        f'./devices/arduino_code/{sketch}/{sketch}.ino',
    ]
    
    # Flashing command for arduino-cli
    flashing_command = [
        'arduino-cli',
        'upload',
        '-p',
        '/dev/ttyUSB0',
        '--fqbn',
        f'{fqbn}',
        f'./devices/arduino_code/{sketch}',
    ]

    try:
        # Run the compilation process        
        compilation_process = subprocess.run(compilation_command)
        
        if compilation_process.returncode == 1:
            raise Exception(f'Error in compiling the device script')

        # Check if compilation failed
        flash_process = subprocess.run(flashing_command, 
                                       check=True, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE
        )

        # Check for any errors during flashing
        if flash_process.stderr != b'':
            raise Exception(f'{flash_process.stderr}')
        
    except subprocess.CalledProcessError as e:
        # Handle any errors raised during the subprocess calls
        raise Exception(f'Error in flashing the device: {e}')


def parse_device_serial(data):
    '''Parses device serial from JSON data.'''

    try:
        # Deserialize the JSON data
        deserialized_message = json.loads(data)
        
        # Retrieve the device serial from the deserialized message
        device_serial = deserialized_message.get('serial', None)

        if not device_serial:
            raise DeviceUnknownResponseException
        
        return device_serial

    # Handle JSON decoding error and raise an exception
    except json.JSONDecodeError:
        raise DeviceUnknownResponseException
