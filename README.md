# Device Management Service

## Overview

This Django project serves as the device management microservice of this home automation project. It allows for the management of devices, rooms, sensors, and provides an API endpoint for flashing Arduino devices over a serial connection. Additionally, it includes an API view for retrieving device information based on serial communication and an API view for sending commands to sensors.

## Features

- **Device Management**: CRUD operations for devices, rooms, and sensors that include creating rooms, assign rooms to devices, assign desired names to devices or sensors, etc.

- **Flash Serial Device API Endpoint**: An API endpoint for flashing Arduino devices over a serial connection with the appropriate WiFi credentials (device connected to server via USB).

- **Get Serial Device API Endpoint**: An API endpoint for retrieving device information based on the serial communication (device connected to server via USB).

- **Send Command To Sensor API Endpoint**: An API endpoint for sending commands to sensors over MQTT using the appropriate topics.

- **Device Status Updater**: A Django management command that starts an MQTT listener and updates device statuses on database based on the related to status MQTT messages sent by devices.

- **Data Population**: A Django management command that populates the database with device data from a JSON file. This command is for emulating the project's functionality as a product shipment, where predefined devices are shipped with a preconfigured JSON file.

## API Endpoints

### Rooms API

- **Endpoint**: /api/rooms/
- **Methods**: GET, POST, PUT, PATCH

### Devices API

- **Endpoint**: /api/devices/
- **Methods**: GET, POST, PUT, PATCH

### Sensors API

- **Endpoint**: /api/sensors/
- **Methods**: GET, POST, PUT, PATCH

### Flash Serial Device API

- **Endpoint**: /api/flash/<int:id>/
- **Methods**: POST
- **Description**: Flash an Arduino device over a serial connection.

### Get Serial Device API

- **Endpoint**: /api/serial/
- **Methods**: GET
- **Description**: Retrieve device information based on serial communication.

### Send Command To Sensor API

- **Endpoint**: /api/command/
- **Methods**: POST
- **Description**: Send a command to a sensor.
