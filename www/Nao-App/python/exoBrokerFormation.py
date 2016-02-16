# -*- encoding: UTF-8 -*-

from naoqi import *
import 
class BasicModuleClass(ALModule):
  """module description"""

  def start(self):
    """method description  (mandatory to have the method published)"""
    self.reco = ALProxy("ALSpeechRecognition")
    #self.reco.setWordListAsVocabulary(["bonjour","assis","debout","couché"])
    memory=ALProxy("ALMemory")
    memory.subscribeToEvent("WordRecognized",self.getName(),"callback")

  def finish(self):
    """method description  (mandatory to have the method published)"""
    memory=ALProxy("ALMemory")
    memory.unsubscribeToEvent("WordRecognized",self.getName())

  def callback(self,var,val,msg):
    """method description  (mandatory to have the method published)"""
    print val[0]
    print val[1]
    if val[1]>0.3 and val[3]<0.25:
		self.memory.raiseEvent(val[0],"debout")
		print val[0]

# un module doit être dans un broker, on doit créer un broker en gros uniquement
# si on doit accéder à un module qui n'est pas dans naoqi (sur notre pc par exemple)

if __name__=="__main__":
  broker=ALBroker("localbroker","0.0.0.0",9559,config.ipnao,9559)

  # Instantiate the module
  global BasicModule
  BasicModule=BasicModuleClass("BasicModule")

  # Wait indefinitely
  while True: pass
