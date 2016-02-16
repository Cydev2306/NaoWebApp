from naoqi import ALProxy
import config
tts = ALProxy("ALTextToSpeech", config.ipnao, 9559)
tts.say("Hello, world!")
