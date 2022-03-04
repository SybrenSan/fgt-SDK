#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Standard priming protocol

"""

import time
from Fluigent.SDK import *

## Read pressure value
pressureMeasurement = fgt_get_pressure(0)
print('Current pressure value: {}'.format(pressureMeasurement))

valvePosition = fgt_get_valvePosition(0)
print('Current valve position: {}'.format(valvePosition))

time.sleep(30)

flow_rates = {}

## Prime fluidic channels
fgt_set_pressure(0,20)
fgt_set_valvePosition(0,10)
time.sleep(180)
fgt_set_valvePosition(0,9)
time.sleep(180)

fgt_set_valvePosition(0,2)
time.sleep(180)
flow_rates['position 2'] = fgt_get_sensorValue(0)
print('Flow rate valve position 2: {:.2f}'.format(flow_rates['position 2']))

fgt_set_valvePosition(0,6)
time.sleep(120)
flow_rates['position 6'] = fgt_get_sensorValue(0)
print('Flow rate valve position 6: {:.2f}'.format(flow_rates['position 6']))

fgt_set_valvePosition(0,5)
time.sleep(120)
flow_rates['position 5'] = fgt_get_sensorValue(0)
print('Flow rate valve position 5: {:.2f}'.format(flow_rates['position 5']))

fgt_set_valvePosition(0,4)
time.sleep(180)
fgt_set_valvePosition(0,8)
time.sleep(180)

fgt_set_pressure(0,5)
