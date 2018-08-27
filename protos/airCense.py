#!/usr/bin/env python

import paho.mqtt.client as mqtt
import sys
import json
import requests
import base64
from influxdb import InfluxDBClient
import time

import airCenseLora_pb2

influxClient = InfluxDBClient('127.0.0.1','8086','root','root','airCense')
rxmsg = airCenseLora_pb2.airCenseProto()

# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("application/1/node/70b3d58ff0031df2/rx")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

	decodedData = str(base64.b64decode(json.loads(str(msg.payload))["data"]))
	
	rxmsg.ParseFromString(decodedData)
	print ''
	print 'CARBON DIOXIDE = ' +str(rxmsg.CO2) + ' PPM'
	print 'CARBON MONOXIDE =  {0:.3f}'.format(rxmsg.CO) + ' PPM'
	print 'NITROGEN DIOXIDE =  {0:.3f}'.format(rxmsg.NO2) + ' PPM'
	print 'TEMPERATURE =  {0:.3f}'.format(rxmsg.temperature) + ' Deg C'
	print 'HUMIDITY =  {0:.3f}'.format(rxmsg.humidity) + ' %RH'
	print 'PM2_5 = {0:.3f}'.format(rxmsg.PM2_5) + ' ugm3'
	print 'PM10 = {0:.3f}'.format(rxmsg.PM10) + ' ugm3'
	print ''
	
	
	epochTime = int(time.time()) * 1000000000
	series  = []
	pointValues = {
		"time": epochTime,
		"measurement": "CO2",
		'fields': {
			'value': rxmsg.CO2,
		},
		'tags': {
			"sensorName": "CO2",
		},
	}
	pointValues = {
		"time": epochTime,
		"measurement": "CO",
		'fields': {
			'value': rxmsg.CO,
		},
		'tags': {
			"sensorName": "CO",
		},
	}
	pointValues = {
		"time": epochTime,
		"measurement": "NO2",
		'fields': {
			'value': rxmsg.NO2,
		},
		'tags': {
			"sensorName": "NO2",
		},
	}
	pointValues = {
		"time": epochTime,
		"measurement": "CO2",
		'fields': {
			'value': rxmsg.CO2,
		},
		'tags': {
			"sensorName": "CO2",
		},
	}
	pointValues = {
		"time": epochTime,
		"measurement": "temperature",
		'fields': {
			'value': rxmsg.temperature,
		},
		'tags': {
			"sensorName": "temperature",
		},
	}
	pointValues = {
		"time": epochTime,
		"measurement": "humidity",
		'fields': {
			'value': rxmsg.humidity,
		},
		'tags': {
			"sensorName": "humidity",
		},
	}
	pointValues = {
		"time": epochTime,
		"measurement": "PM2_5",
		'fields': {
			'value': rxmsg.PM2_5,
		},
		'tags': {
			"sensorName": "PM2_5",
		},
	}
	pointValues = {
		"time": epochTime,
		"measurement": "PM10",
		'fields': {
			'value': rxmsg.PM10,
		},
		'tags': {
			"sensorName": "PM10",
		},
	}
	series.append(pointValues)


	print series
	
	influxClient.write_points(series,time_precision='n')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("loraserver","loraserver")

client.connect("gateways.rbccps.org", 1883, 60)
client.loop_forever()


