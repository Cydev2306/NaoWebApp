# -*- encoding: UTF-8 -*-
# Before running this command please check your PYTHONPATH is set correctly to the folder of your pynaoqi sdk.
from naoqi import ALProxy
import time
import config
# Set the IP address of your NAO.
ip = config.ipnao

# Connect to ALSonar module.
tts = ALProxy("ALTextToSpeech", ip, 9559)
sonarProxy = ALProxy("ALSonar", ip, 9559)

# Subscribe to sonars, this will launch sonars (at hardware level) and start data acquisition.
sonarProxy.subscribe("myApplication")

#Now you can retrieve sonar data from ALMemory.
memoryProxy = ALProxy("ALMemory", ip, 9559)

# Get sonar left first echo (distance in meters to the first obstacle).
print memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")
tts.say('coucou')
# Same thing for right.
print memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")
#print memoryProxy.getDataListName()


try:
	while True:
		time.sleep(1)
		# Get sonar left first echo (distance in meters to the first obstacle).
		print memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")
		tts.say('coucou')
		# Same thing for right.
		print memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")
except KeyboardInterrupt:
	print
	print "Interrupted by user, shutting down"
	sonarProxy.unsubscribe("myApplication")
