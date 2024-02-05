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

