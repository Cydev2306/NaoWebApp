import time
from array import array
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule


#**************
# Module class
#**************

class BasicAudioModule(ALModule):
  """basic audio module"""

  def __init__(self,name):
    ALModule.__init__(self,name)
    self.isRunning=True
    self.audio=ALProxy("ALAudioDevice")
    self.memory=ALProxy("ALMemory")
    try:
      self.audio.unsubscribe(self.getName())
      print 'Removed existing subscription'
    except:
      pass
    self.audio.subscribe(self.getName())


  def processSoundRemote(self,nchannels,nsamples,data):
    """callback when new remote sound data to process""" # mandatory annotation so that the method is published as a module method
    
    # Retrieve sound data (string buffer)
    print 'Remote sound data nchannels=',nchannels,' nsamples=',nsamples

    # Convert into an array of signed short
    # Array contains all 4 microphones samples as interleaved data: s0m0 s0m1 s0m2 s0m3 s1m0 ...
    # Microphones 0:left 1:right 2:front 3:rear
    
    dataarray=array('h',data)
    max = 0
    for i in range(0,nsamples):
      front=abs(dataarray[i*4+2])
      if front>10000:
        print front
        print "significantsound"
        self.memory.raiseMicroEvent("significantsound",front)
        return
      if front>max:
		  max=front
    print max
        

  def exit(self):
    self.audio.unsubscribe(self.getName())
    self.isRunning=False
    ALModule.exit(self)

    
#***********
# Main code
#***********

if __name__=='__main__':
  # Parameters
  moduleName="BasicAudio"
  NAO_IP="matthnao.local"
  NAO_PORT=9559

  LOCALBROKER_NAME="localbroker"
  LOCALBROKER_IP="0.0.0.0"
  LOCALBROKER_PORT=9559

  # Create a local broker
  broker=ALBroker(LOCALBROKER_NAME,LOCALBROKER_IP,LOCALBROKER_PORT,NAO_IP,NAO_PORT)

  # Create a module instance
  BasicAudio=BasicAudioModule(moduleName)


  try:
    while BasicAudio.isRunning: time.sleep(1)
  except:
    print "Cleaning up"
    BasicAudio.exit()

