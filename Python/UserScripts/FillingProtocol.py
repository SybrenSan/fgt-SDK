#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Standard bioFET filling protocol

"""

import time
from Fluigent.SDK import *

## Get sensor range
minPressure, maxPressure = fgt_get_pressureRange(0)
minSensor, maxSensor = fgt_get_sensorRange(0)
print(minSensor)
print(maxSensor)

## Read pressure value
pressureMeasurement = fgt_get_pressure(0)
print('Current pressure value: {}'.format(pressureMeasurement))

valvePosition = fgt_get_valvePosition(0)
print('Current valve position: {}'.format(valvePosition))

time.sleep(30)

flow_rates = {}

fgt_set_pressure(0,300)
time.sleep(5)

## Inject IPA
fgt_set_valvePosition(0,10)
time.sleep(300)

## Inject 50% IPA/DIW
fgt_set_valvePosition(0,9)
time.sleep(200)

## Inject buffer
fgt_set_valvePosition(0,2)
time.sleep(200)
fgt_set_pressure(0,500)
time.sleep(150)

fgt_set_sensorRegulationResponse(0,200)
fgt_set_sensorRegulation(0,0,25)

