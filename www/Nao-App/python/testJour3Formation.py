# -*- encoding: UTF-8 -*-
#import motion
#import almath
import time
import naoqi
from naoqi import *
import config

#Cartesian control api

# comme on est pas dans choregraphe faut spécifier l'ip et le port au module pour le broker local
# un broker contient des modules, la c'est le broker local
ip = config.ipnao
port = 9559

posture = ALProxy("ALRobotPosture",ip,port)
motion = ALProxy("ALMotion",ip,port)
memory = ALProxy("ALMemory",ip,port)

posture.goToPosture("Crouch",0.6)

#position = [0.15,0,0.3,0,0,0]
#motion.setPosition("RArm",2,position,0.4,7)

time.sleep(5)

#for i in range(0,10):

	#position = [0,0,0.01,0,0,0]
	#motion.changePosition("RArm",2,position,0.2,7)
	#time.sleep(2)

posture.goToPosture("StandInit",0.6)

for i in range(0,10):
	left = str(memory.getData("leftFootTotalWeight"))
	right = str(memory.getData("rightFootTotalWeight"))
	if(left>5):
		positionTorsoZ = [0,0,0.005,0,0,0]
		motion.changePosition("RLeg",2,positionTorsoZ,0.2,7)
		time.sleep(2)
		print "left = "+left
		print "right = "+right
	else:
		positionTorsoY = [0,-0.01,0,0,0,0]
		motion.changePosition("Torso",2,positionTorsoY,0.2,7)
		time.sleep(2)
		print "left = "+left
		print "right = "+right

# motion.rest() desactive tous les moteurs
motion.rest()
# x,y,z,wx,wy,wz
# poid faible 1,1,1,0,0,0
# 1+2+4 = 7
# changePosition et setPosition sont des fonctions non bloquantes
# elles se referent au referentiel au niveau de ses pieds.
# changePosition rajoute ce qu'on lui passe a la position actuelle
# les deux fonctions calculent les trajectoires, en fonction de tous
# les moteurs, ça garde un minimum l'equilibre et on dirige les les moteurs
# d'une partie du corps.
# Torso, RArm etc...
