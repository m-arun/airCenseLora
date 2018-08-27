#!/usr/bin/env python

import paho.mqtt.client as mqtt
import sys
import json
import requests
import base64

import time

import airCenseLora_pb2


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
	print('')
	print ('CARBON DIOXIDE = ' +str(rxmsg.CO2) + ' PPM')
	print ('CARBON MONOXIDE =  {0:.3f}'.format(rxmsg.CO) + ' PPM')
	print ('NITROGEN DIOXIDE =  {0:.3f}'.format(rxmsg.NO2) + ' PPM')
	print ('TEMPERATURE =  {0:.3f}'.format(rxmsg.temperature) + ' Deg C')
	print ('HUMIDITY =  {0:.3f}'.format(rxmsg.humidity) + ' %RH')
	print ('PM2_5 = {0:.3f}'.format(rxmsg.PM2_5) + ' ugm3')
	print ('PM10 = {0:.3f}'.format(rxmsg.PM10) + ' ugm3')
#	print 'BAROMETRIC PRESSURE = {0:.3f}'.format(rxmsg.barometricPressure) + ' mb'
#	print 'RELATIVE PRESSURE =  {0:.3f}'.format(rxmsg.relativePressure) + ' mb'
#	print 'PARTICULATE MATTER 10 =  {0:.3f}'.format(rxmsg.PM10) + ' Particles/0.01cf'
	print ('')
	
	f = open('airCenseLog.csv','a')
	epochTime = str(int(time.time()))
	f.write(epochTime)
	f.write(',')
	f.write(str(rxmsg.CO2)+',')
	f.write('{0:.3f}'.format(rxmsg.CO) + ',')
	f.write('{0:.3f}'.format(rxmsg.NO2) + ',')
	f.write('{0:.3f}'.format(rxmsg.temperature) + ',')
	f.write('{0:.3f}'.format(rxmsg.humidity) + ',')
	f.write('{0:.3f}'.format(rxmsg.PM2_5) + ',')
	f.write('{0:.3f}'.format(rxmsg.PM10) + '')
	#f.write('{0:.3f}'.format(rxmsg.barometricPressure) + ',')
	#f.write('{0:.3f}'.format(rxmsg.relativePressure) + '')
	f.write("\n")
	f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("loraserver","loraserver")

client.connect("gateways.rbccps.org", 1883, 60)
client.loop_forever()


