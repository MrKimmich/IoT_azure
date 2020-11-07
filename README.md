# IoT_azure

### [Quickstart: Send telemetry from a device to an IoT hub and read it with a back-end application (Python)](https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python)
### [Visualize real-time sensor data from Azure IoT Hub using Power BI](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-live-data-visualization-in-power-bi)
### [GetStarted GitHub Repo](https://github.com/Azure-Samples/azure-iot-samples-python)

## Install below packages on Raspberry Pi
`sudo pip3 install azure-iot-device`</br>
`sudo pip3 install azure-iot-hub`</br>
`sudo pip3 install azure-iothub-service-client`</br>
`sudo pip3 install azure-iothub-device-client`</br>


Make sure you run your code with Python3

### Now before you run the Python program create an azure shell (CLI). When you open it for the first time it will ask you to create storage.
 
### See below to add the extension:

`az extension add --name azure-cli-iot-ext`</br>

### To start device monitor
`az iot hub monitor-events --hub-name MSR0806 --device-id MyRPi`

## Azure CLI for Windows
Download and Install
https://www.aka.ms/installazurecliwindows

### Open Command prompt
`az`</br>
#### Firstly login to Azure account
`az login`
#### Next set the subscription
`az account set --subscription "Free Trail"`</br>
#### Adding extensions for IoT
`az extension add --name azure-iot`</br>

## Event Hubs-compatible endpoint, Event Hubs-compatible path, and service primary
`az iot hub show --query properties.eventHubEndpoints.events.endpoint --name {YourIoTHubName}`</br>

`az iot hub show --query properties.eventHubEndpoints.events.path --name {YourIoTHubName}`</br>

`az iot hub policy show --name service --query primaryKey --hub-name {YourIoTHubName}`</br>

## Preparing your Raspberry Pi to Talk with the Accelerometer

1.Before we can get our Raspberry Pi to retrieve data from our ADXL345 Accelerometer, there are a few changes we must make to the Pi’s configuration.

`sudo apt-get update`</br>
`sudo apt-get upgrade`</br>

2.Once the Raspberry Pi has finished updating, we will need to go ahead and launch the Raspberry configuration tool so that we can enable I2C on the Raspberry Pi.

Run the following command to launch the raspi configuration tool.

`sudo raspi-config`</br>

3.On this screen, you need to head to the "5 Interfacing Options" menu. 
You can navigate the raspi-config tools menus by using the arrow keys. Use the ENTER key to select particular options.

4.Now within the interfacing options menu go ahead and select "P5 I2C". 
When asked if you would like to enable the "ARM I2C interface", select "YES".

5.After enabling the I2C interface, you will need to restart your Raspberry Pi by running the following command.

`sudo reboot`.</br>

6. Now that we have enabled I2C and restarted the Raspberry Pi, we can now proceed to install the packages that we will rely on to talk with our accelerometer.
Run the following command to install.

`sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y`</br>

7.With all our required packages installed let’s now check to see whether our Raspberry Pi can see our ADXL345 Accelerometer.
From this command, you should see a fair bit displayed on the command line. Within this result, you should at least see a number such as “53“.

`sudo i2cdetect -y 1`</br>

8.With all the packages that we need now installed to the Raspberry Pi, we can now proceed to working directory and install Adafruit’s ADXL34x Python library.
Run following command with pip command.

`sudo pip3 install adafruit-circuitpython-ADXL34x`</br>

## Preparing for DHT11 sensor

To install the Adafruit DHT11 library:

1. Enter this at the command prompt to download the library:

`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`</br>

2. Change directories with:

`cd Adafruit_Python_DHT`</br>

3. Now enter this:

`sudo apt-get install build-essential python-dev`</br>

4. Then install the library with:

`sudo python setup.py install`</br>




