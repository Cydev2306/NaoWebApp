#!/usr/bin/python
# -*- encoding: UTF-8 -*-

from naoqi import *
import requests, os
import json
import config

url = "http://weather.nshub.net/forecast/YAH/test_app?env=prod&bs_code=weather&latitude=49.847066&longitude=3.289837"
rs = requests.get(url, params=None, data=None)

decoded = json.loads(rs.content)

#print json.dumps(decoded, sort_keys=True, indent=4)
#print decoded['forecast']['weather']['temperature']['value']

tts = ALProxy("ALTextToSpeech", config.ipnao, 9559)
tts.say("Aujourd'hui à saint quentin, il fait "+str(decoded['forecast']['weather']['temperature']['value'])+" degré")
