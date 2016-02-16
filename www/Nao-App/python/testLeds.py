import sys
from naoqi import ALProxy
import config
IP = config.ipnao
PORT = 9559
try:
    proxy = ALProxy("ALLeds", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALLeds"
    print "Error was: ",e
    sys.exit(1)

# Example showing a one second rasta animation
duration = 5.0
proxy.rasta(duration)
