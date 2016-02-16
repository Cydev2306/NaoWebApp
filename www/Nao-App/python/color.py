# -*- encoding: UTF-8 -*-

import sys
import time
import random
import color
import motion
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech",config.ipnao,9559)
sr = ALProxy("ALSpeechRecognition",config.ipnao,9559)
memProxy = ALProxy("ALMemory",config.ipnao,9559)
motion = ALProxy("ALMotion",config.ipnao,9559)

sr.setVocabulary(["oui","non","rouge","bleu","vert","jaune","orange","rose","blanc"],True)
sr.setAudioExpression(True)
sr.setVisualExpression(True)

fini = False
x = "WordRecognized"
cpt = 3

def onWordRecognized(x,total):
    """Ici on regarde le mot reconnu si l'indice de fiabilité est supérieur à 0.5 """
    retVal = memProxy.getData("WordRecognized")
    print x, retVal[0], retVal[1]
    print total
    if(retVal[0] != "" and retVal[1]>0.5):
      if(retVal[0] == "rouge"):
		  return True
      elif retVal[0] == "bleu":
		  return True
      elif retVal[0] == "vert":
		  return True
      elif retVal[0] == "jaune":
		  return True
      elif retVal[0] == "orange":
		  return True
      elif retVal[0] == "rose":
		  return True
      elif retVal[0] == "blanc":
		  return True
      elif retVal[0] == "oui":
		  return "oui"
      elif retVal[0] == "non":
		  return "non"

while fini == False :

	""" On met ou on remet reussi à False pour continuer """
	reussi = False

	while reussi == False :

		"""On demande le résultat"""
		tts.say("Je peux controler les lumières de ces leds, veux tu essayer ? Vas y, dis moi une couleur")
		sr.subscribe("Jouer")
		time.sleep(3)
		if(onWordRecognized(x)):
			"""Si le résultat est reconnu"""
			reussi = True
			sr.unsubscribe("Jouer")
			motion.rest()
			tts.say("ça a marché ! Veux-tu réessayer ?")
			sr.subscribe("Rejouer")
			time.sleep(3)
			if(onWordRecognized(x) == "non"):
				fini = True
			sr.unsubscribe("Rejouer")
		else:
			"""Si le résultat n'est pas reconnu """
			sr.unsubscribe("Jouer")
			""" On regarde le nombre d'essais restant """
			if cpt == 0 :
				""" On relance une nouvelle couleur ou on termine le programme """
				tts.say("Ce n'est pas très grave, on recommence ! Veux-tu réessayer ?")
				sr.subscribe("Rejouer")
				time.sleep(3)
				if(onWordRecognized(x) == "non"):
					fini = True
				sr.unsubscribe("Rejouer")
				reussi = True
			else :
				tts.say("Desole je ne connais pas cette couleur")

tts.say("Merci d'avoir essaye les lumières connectes avec avec moi ! On rejoue quand tu veux !")
