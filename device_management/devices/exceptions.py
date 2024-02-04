class DeviceGenericException(Exception):
    pass


class DeviceNotFoundException(DeviceGenericException):
    def __init__(self, message='Error. Please make sure a valid device is connected or that /dev/ttyUSB0 is not in use by another process.'):
        self.message = message
        super().__init__(self.message)


class DeviceNoResponseException(DeviceGenericException):
    def __init__(self, message='A device was found but it is unresponsive. Ensure that a compatible device is properly connected to /dev/ttyUSB0.'):
        self.message = message
        super().__init__(self.message)


class DeviceUnknownResponseException(DeviceGenericException):
    def __init__(self, message='Unknown response from connected device. Ensure that a compatible device is properly connected to /dev/ttyUSB0.'):
        self.message = message
        super().__init__(self.message)


class DeviceUnknownSerialException(DeviceGenericException):
    def __init__(self, message='Device\'s serial could not be found in the database.'):
        self.message = message
        super().__init__(self.message)
