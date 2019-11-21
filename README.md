# Real-time Data Visualization (an import from https://github.com/r07921078/rpi_realtime_3g for a lab provided for Taipei Municipal Jianguo High School)
## IP
*192.168.130.xxx (Web Server-sensor gateway)
*localhost (Sensor device)

**You need change ip address(in source code) dependent on your "network environment"**

## Web server - sensor gateway
```
$ pip3 install websockets
$ sudo apt-get update
$ sudo apt-get install apache2
```

move "plot_3gAcc_from_websocket.html" to "/var/www/html/" <br/>
move "plot_3gAcc_from_websocket_xyz.html" to "/var/www/html/"

```
$ python3 ws_server.py
```

## Sensor device
### w/o ADXL345 Sensor
```
$ python3 socket_server_random.py
```

### w/ ADXL345 Sensor

ref: https://www.instructables.com/id/how-to-use-the-ADXL345-on-Raspberry-pi/

1. 4 connections: 


| RPI | ADXL345 |
| ---- | --- |
| GND  | GND |
| 3V   | 3V3 |
| SDA  | SDA |
| SCL  | SCL |


2. sudo nano /etc/modules & add
    * i2c-bcm2708
    * i2c-dev
3. sudo raspi-config & enable I2C
3. sudo reboot
4. sudo apt-get install python-smbus i2c-tools git-core
5. sudo i2cdetect -y 1
    * you should not get any errors and see a device at address 53

and then

```
$ python3 socket_server.py
```

## PDF/PPT
* http://hpc.ee.ntu.edu.tw/html/sd/DataVisual-Lab-1121-2019/IoT-Data-Visualization-Lab-1121.pdf
* https://docs.google.com/presentation/d/17gcLdMVilcXN4QGtei15g-6nFRCPQJV9zVY96pl77yE/edit?usp=sharing


### reference
* http://www.whatimade.today/realtime-graphs-using-ploty-and-websockets/
* https://github.com/dannyvai/plotly_websocket_example
* https://github.com/google/pywebsocket
* https://websockets.readthedocs.io/en/stable/intro.html
* https://realpython.com/python-sockets/
* https://canvasjs.com/docs/charts/basics-of-creating-html5-chart/
* https://canvasjs.com/html5-javascript-dynamic-chart/
* https://www.instructables.com/id/how-to-use-the-ADXL345-on-Raspberry-pi/
* https://github.com/pimoroni/adxl345-python

