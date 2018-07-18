# IncubatorMonitoringSystem

Incubator Monitoring System for the Raspberry Pi.

## Introduction
This Program allows the user the ability to monitor the envoronmental condition of chicken eggs, without the need to be present at the site of the incubator. 

## Deployement

## Requirements
In order to run this project the user must have all of the following:
* Raspberry Pi 3B+ (Has not been tested on earlier Pi models, or Pi Zero)
** The Raspberry Pi must also run Raspbian Stretch in order to use the GPIO
* Python 3.6.5 (To run Django)
* Django 2.0.5


Currently this program only supports the DHT11 for reading temperature data. However proposed updates will include the Bosch BME 280 and Dallas one wire DB12B20 as well as support for multiple sensors.
