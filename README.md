# IoT_azure

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
