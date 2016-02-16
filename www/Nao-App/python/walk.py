import sys
# -*- encoding: UTF-8 -*-

import time
import urllib
from naoqi import ALProxy
import config
while True :

	opener = urllib.FancyURLopener({})
	f = opener.open("http://myfristnaoapp.appspot.com/task/task?mdp=admin&login=admin@gmail.com")
	cmd = f.read()
	if cmd=="standup":
		postureProxy = ALProxy("ALRobotPosture",config.ipnao, 9559)
		postureProxy.goToPosture("Stand", 1)
	elif cmd == "sitdown":
		postureProxy = ALProxy("ALRobotPosture",config.ipnao, 9559)
		postureProxy.goToPosture("Sit", 1)
		p = ALProxy("ALMotion",config.ipnao, 9559)
		p.rest()
	elif cmd == "crouch":
		postureProxy = ALProxy("ALRobotPosture",config.ipnao, 9559)
		postureProxy.goToPosture("Crouch", 1)
		p = ALProxy("ALMotion", "nao.local", 9559)
		p.rest()
	elif cmd == "gangnamstyle":
		behaviorManagerProxy = ALProxy("ALBehaviorManager",config.ipnao, 9559)
		behaviorManagerProxy.runBehavior("gangnamstyle")
	elif cmd == "caravanpalace":
		behaviorManagerProxy = ALProxy("ALBehaviorManager",config.ipnao, 9559)
		behaviorManagerProxy.runBehavior("caravanpalace")
	elif cmd == "grabobject":
		behaviorManagerProxy = ALProxy("ALBehaviorManager",config.ipnao, 9559)
		behaviorManagerProxy.runBehavior("grabObject")
	elif cmd == "lyingbelly":
		postureProxy = ALProxy("ALRobotPosture",config.ipnao, 9559)
		postureProxy.goToPosture("LyingBelly", 1)
		p = ALProxy("ALMotion",config.ipnao, 9559)
		p.rest()
	elif cmd == "lyingback":
		postureProxy = ALProxy("ALRobotPosture",config.ipnao, 9559)
		postureProxy.goToPosture("LyingBack", 1)
		p = ALProxy("ALMotion",config.ipnao, 9559)
		p.rest()
