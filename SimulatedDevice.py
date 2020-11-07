# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time
import Adafruit_DHT
import board
import busio
import adafruit_adxl34x

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio=17

# Here we utilize the “busio” library to prepare an I2C connection for our current boards SCL and SDA pins
i2c = busio.I2C(board.SCL, board.SDA)

# We now instantiate the ADXL345 library into our “accelerometer” object. 
# We will utilize this object to read and obtain information from our sensor.
# Into the constructor for the library, we pass in our I2C handle
accelerometer = adafruit_adxl34x.ADXL345(i2c)

# Using the Python Device SDK for IoT Hub:
# https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "{Your IoT hub device connection string}"

# Define the JSON message to send to IoT Hub.
MSG_TXT = '{
    {
        "temperature": {temperature},
        "humidity": {humidity},
        "x_axis": {x_axis},
        "y_axis": {y_axis},
        "z_axis": {z_axis}
    }
}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Use read_retry method. This will retry up to 15 times to
            # get a sensor reading (waiting 2 seconds between each retry).
            humidity, temprature = Adafruit_DHT.read_retry(sensor, gpio)
            
            #X, Y, and Z acceleration values that have been retrieved from the accelerometer by the library.
            x_axis, y_axis, z_axis = accelerometer.acceleration()
            
            if humidity and temprature and x_axis and y_axis and z_axis:
                msg_txt_formatted = MSG_TXT.format(temperature = temperature, humidity = humidity, x_axis = x_axis, y_axis = y_axis, z_axis = z_axis)
                message = Message(msg_txt_formatted)
            else:
                print('Failed to get reading. Try again!')
            
            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if temperature > 30:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
