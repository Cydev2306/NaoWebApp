# -*- encoding: UTF-8 -*-

'''Wake up: sets Motor on and, if needed, goes to initial position'''
import time
import sys
import naoqi
from naoqi import *
import config
def main():

	try:
		motionProxy = ALProxy("ALMotion",config.ipnao,9559)
	except Exception, e:
		print "Could not create proxy to ALMotion"
		print "Error was: ", e

	motionProxy.getPostureList();

main()
