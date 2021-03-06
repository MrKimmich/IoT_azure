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
