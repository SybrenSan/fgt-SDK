#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get Instrument Info

Retrieve information about connected Fluigent 
instruments: type, controller, serial number, unique ID...
	
Requires at least one Fluigent pressure or sensor module

"""

from Fluigent.SDK import *

# Detect all controllers
SNs, types = fgt_detect()
controllerCount = len(SNs)
print('Number of controllers detected: {}'.format(controllerCount))

# List all found controllers' serial number and type
for i, sn in enumerate(SNs):
    print('Detected instrument at index: {}, ControllerSN: {}, type: {}'\
        .format(i, sn, str(types[i])))

print('')

## Initialize specific instruments
# Initialize only specific instrument controllers here If you do not want
# a controller in the list or if you want a specific order (e.g. LineUP
# before MFCS instruments), rearrange parsed SN table
fgt_init(SNs)

## Get the number of channels of each type

# Get total number of initialized pressure channels
print('Total number of pressure channels: {}'.format(fgt_get_pressureChannelCount()))

# Get total number of initialized sensor channels
print('Total number of sensor channels: {}'.format(fgt_get_sensorChannelCount()))

# Get total number of initialized valve channels
print('Total number of valve channels: {}'.format(fgt_get_valveChannelCount()))

print('')
    
## Get detailed information about all controllers

controllerInfoArray = fgt_get_controllersInfo()
for i, controllerInfo in enumerate(controllerInfoArray):
    print('Controller info at index: {}'.format(i))
    print(controllerInfo)
    print('')

## Get detailed information about all pressure channels

pressureInfoArray = fgt_get_pressureChannelsInfo()
for i, pressureInfo in enumerate(pressureInfoArray):
    print('Pressure channel info at index: {}'.format(i))
    print(pressureInfo)
    print('')

minPressure, maxPressure = fgt_get_pressureRange(0)
print(minPressure)
print(maxPressure)

## Get detailed information about all sensors

sensorInfoArray, sensorTypeArray = fgt_get_sensorChannelsInfo()
for i, sensorInfo in enumerate(sensorInfoArray):
    print('Sensor channel info at index: {}'.format(i))
    print(sensorInfo)
    print("Sensor type: {}".format(sensorTypeArray[i]))
    print('')

minSensor, maxSensor = fgt_get_sensorRange(0)
print(minSensor)
print(maxSensor)

## Get detailed information about all valves
    
valveInfoArray, valveTypeArray = fgt_get_valveChannelsInfo()
for i, valveInfo in enumerate(valveInfoArray):
    print('Valve channel info at index: {}'.format(i))
    print(valveInfo)
    print("Valve type: {}".format(valveTypeArray[i]))
    print('')

## Close the session
fgt_close()
