# -*- encoding: UTF-8 -*-

import sys
import time
import random
import config
import motion
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech",config.ipnao,9559)
sr = ALProxy("ALSpeechRecognition",config.ipnao,9559)
memProxy = ALProxy("ALMemory",config.ipnao,9559)
motion = ALProxy("ALMotion",config.ipnao,9559)

sr.setVocabulary(["oui","non","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","douze","quatorze","quinze","seize","dix-huit","vingt","vingt-et-un","vingt-quatre","vingt-cinq","vingt-sept","vingt-huit","trente","trente-deux","trente-cinq","trente-six","quarante","quarante-deux","quarante-cinq","quarante-huit","quarante-neuf","cinquante","cinquante-quatre","cinquante-six","soixante","soixante-trois","soixante-quatre","soixante-dix","soixante-douze","quatre-vingts","quatre-vingt-un","quatre-vingt-dix","cent"],True)
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
      if(retVal[0] == "un" and total == 1):
		  return True
      elif retVal[0] == "deux" and total == 2:
		  return True
      elif retVal[0] == "trois" and total == 3:
		  return True
      elif retVal[0] == "quatre" and total == 4:
		  return True
      elif retVal[0] == "cinq" and total == 5:
		  return True
      elif retVal[0] == "six" and total == 6:
		  return True
      elif retVal[0] == "sept" and total == 7:
		  return True
      elif retVal[0] == "huit" and total == 8:
		  return True
      elif retVal[0] == "neuf" and total == 9:
		  return True
      elif retVal[0] == "dix" and total == 10:
		  return True
      elif retVal[0] == "douze" and total == 12:
		  return True
      elif retVal[0] == "quatorze" and total == 14:
		  return True
      elif retVal[0] == "quinze" and total == 15:
		  return True
      elif retVal[0] == "seize" and total == 16:
		  return True
      elif retVal[0] == "dix-huit" and total == 18:
		  return True
      elif retVal[0] == "vingt" and total == 20:
		  return True
      elif retVal[0] == "vingt-et-un" and total == 21:
		  return True
      elif retVal[0] == "vingt-quatre" and total == 24:
		  return True
      elif retVal[0] == "vingt-cinq" and total == 25:
		  return True
      elif retVal[0] == "vingt-sept" and total == 27:
		  return True
      elif retVal[0] == "vingt-huit" and total == 28:
		  return True
      elif retVal[0] == "trente" and total == 30:
		  return True
      elif retVal[0] == "trente-deux" and total == 32:
		  return True
      elif retVal[0] == "trente-cinq" and total == 35:
		  return True
      elif retVal[0] == "trente-six" and total == 36:
		  return True
      elif retVal[0] == "quarante" and total == 40:
		  return True
      elif retVal[0] == "quarante-deux" and total == 42:
		  return True
      elif retVal[0] == "quarante-cinq" and total == 45:
		  return True
      elif retVal[0] == "quarante-huit" and total == 48:
		  return True
      elif retVal[0] == "quarante-neuf" and total == 49:
		  return True
      elif retVal[0] == "cinquante" and total == 50:
		  return True
      elif retVal[0] == "cinquante-quatre" and total == 54:
		  return True
      elif retVal[0] == "cinquante-six" and total == 56:
		  return True
      elif retVal[0] == "soixante" and total == 60:
		  return True
      elif retVal[0] == "soixante-trois" and total == 63:
		  return True
      elif retVal[0] == "soixante-quatre" and total == 64:
		  return True
      elif retVal[0] == "soixante-dix" and total == 70:
		  return True
      elif retVal[0] == "soixante-douze" and total == 72:
		  return True
      elif retVal[0] == "quatre-vingts" and total == 80:
		  return True
      elif retVal[0] == "quatre-vingt-un" and total == 81:
		  return True
      elif retVal[0] == "quatre-vingt-dix" and total == 90:
		  return True
      elif retVal[0] == "cent" and total == 100:
		  return True
      elif retVal[0] == "oui":
		  return "oui"
      elif retVal[0] == "non":
		  return "non"

while fini == False :

	"""On détermine une multiplication et on enregistre le résultat """
	chiffreUn = random.randint(1,10)
	chiffreDeux = random.randint(1,10)
	total = chiffreUn * chiffreDeux

	""" On met ou on remet reussi à False pour continuer """
	reussi = False

	while reussi == False :

		"""On demande le résultat"""
		tts.say("Combien font "+str(chiffreUn)+" fois "+str(chiffreDeux)+" ?")
		sr.subscribe("Jouer")
		time.sleep(3)
		if(onWordRecognized(x,total)):
			"""Si le résultat est reconnu"""
			reussi = True
			sr.unsubscribe("Jouer")
			motion.rest()
			tts.say("Bien joué ! Veux-tu rejouer ?")
			sr.subscribe("Rejouer")
			time.sleep(3)
			if(onWordRecognized(x,total) == "non"):
				fini = True
			sr.unsubscribe("Rejouer")
			cpt = 3
		else:
			"""Si le résultat n'est pas reconnu """
			sr.unsubscribe("Jouer")
			cpt = cpt - 1
			""" On regarde le nombre d'essais restant """
			if cpt == 0 :
				""" On relance une nouvelle multiplication ou on termine le programme """
				tts.say("Ce n'est pas très grave, on recommence ! Veux-tu rejouer ?")
				sr.subscribe("Rejouer")
				time.sleep(3)
				if(onWordRecognized(x,total) == "non"):
					fini = True
				sr.unsubscribe("Rejouer")
				cpt = 3
				reussi = True
			else :
				tts.say("Raté ! Il te reste "+str(cpt)+" essais.")

tts.say("Merci d'avoir joué avec moi ! On rejoue quand tu veux !")
