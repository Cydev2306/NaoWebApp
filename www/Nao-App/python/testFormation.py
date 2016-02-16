from naoqi import *
import config
class BasicModuleClass(ALModule):
  """module description"""

  def start(self):
    """method description  (mandatory to have the method published)"""
    memory=ALProxy("ALMemory")
    memory.subscribeToEvent("WordRecognized",self.getName(),"callback")

  def finish(self):
    """method description  (mandatory to have the method published)"""
    memory=ALProxy("ALMemory")
    memory.unsubscribeToEvent("WordRecognized",self.getName())

  def callback(self,var,val,msg):
    """method description  (mandatory to have the method published)"""
    print val

# un module doit être dans un broker, on doit créer un broker en gros uniquement
# si on doit accéder à un module qui n'est pas dans naoqi (sur notre pc par exemple)

if __name__=="__main__":
  broker=ALBroker("localbroker","0.0.0.0",9559,config.ipnao,9559)

  # Instantiate the module
  global BasicModule
  BasicModule=BasicModuleClass("BasicModule")

  # Wait indefinitely
  while True: pass
