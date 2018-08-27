#!/usr/bin/env python

import paho.mqtt.client as mqtt
import sys
import json
import requests
import base64

import airCenseLora_pb2


rxmsg = airCenseLora_pb2.airCenseProto()

# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("application/1/node/70b3d58ff0031dee/rx")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

	decodedData = str(base64.b64decode(json.loads(str(msg.payload))["data"]))
	
	rxmsg.ParseFromString(decodedData)
	print 'CARBON DIOXIDE = ' +str(rxmsg.CO2) + ' PPM'
	print 'CARBON MONOXIDE =  {0:.3f}'.format(rxmsg.CO) + ' PPM'
	print 'NITROGEN DIOXIDE =  {0:.3f}'.format(rxmsg.NO2) + ' PPM'
	print 'TEMPERATURE =  {0:.3f}'.format(rxmsg.temperature) + ' Deg C'
	print ''
	print 'BAROMETRIC PRESSURE = {0:.3f}'.format(rxmsg.barometricPressure) + ' mb'
	print 'RELATIVE PRESSURE =  {0:.3f}'.format(rxmsg.relativePressure) + ' mb'
#	print 'NITROGEN DIOXIDE =  {0:.3f}'.format(rxmsg.NO2) + ' PPM'
#	print 'CARBON MONOXIDE =  {0:.3f}'.format(rxmsg.CO) + ' PPM'
	print 'HUMIDITY =  {0:.3f}'.format(rxmsg.humidity) + ' %RH'
#	print 'CARBON DIOXIDE = ' +str(rxmsg.CO2) + ' PPM'
#	print 'PARTICULATE MATTER 10 =  {0:.3f}'.format(rxmsg.PM10) + ' Particles/0.01cf'
	print ''

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("loraserver","loraserver")

client.connect("gateways.rbccps.org", 1883, 60)
client.loop_forever()


