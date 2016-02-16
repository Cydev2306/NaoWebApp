import time
from naoqi import ALProxy
import config
tts = ALProxy("ALTextToSpeech", config.ipnao, 9559)

tts.setParameter("pitchShift",0)
tts.setParameter("doubleVoice",0)
#tts.setParameter("doubleVoiceLevel",4)
tts.say("je test")
time.sleep(1)

tts.setParameter("pitchShift",0)
tts.say("je test")
time.sleep(1)


#Applies a pitch shifting to the voice
tts.setParameter("pitchShift", 1.5)
#Deactivates double voice
tts.setParameter("doubleVoice", 0.0)

tts.say("Pitch shift and double voice changed")
