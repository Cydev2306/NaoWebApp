# -*- encoding: UTF-8 -*-

'''Cartesian control: Arm trajectory example'''

import sys
import motion
import time
from naoqi import ALProxy
import config

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def GivePen(motionProxy,tts):
    # Ajouter le fait que nao Attrappe le stylo
    position = False
    while (position ==False) :
        tts.say("Donne moi mon stylo s'il te plait")

        joints=["RElbowRoll","RElbowYaw","RHand","RShoulderPitch","RShoulderRoll","RWristYaw"]
        angles=[[0.16878],[0.31136],[1],[ -0.10427],[ -0.10282],[ 1.82387]]
        times=[[1],[1],[1],[1],[1],[1]]
        motionProxy.angleInterpolation(joints,angles,times,True)
        time.sleep(2)
        motionProxy.setAngles("RHand",0,1)
        time.sleep(1.5)

        pos1=motionProxy.getAngles("RHand",True)[0]
        print str(pos1)
        if pos1>0.05:
            tts.say("Merci")
            position = True
            return True
        else:
            print "encore"
            tts.say("Allez")




def main(robotIP):
    ''' Example showing a hand ellipsoid
    Warning: Needs a PoseInit before executing
    '''
    # On essaie les connections aux differents proxys
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        tts = ALProxy("ALTextToSpeech",robotIP,9559)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e



    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)
    # Nao demande & prend le stylo

    if (GivePen(motionProxy,tts)== True):
        tts.say("Je vais te montrer que moi aussi, on peut m'apprendre des choses.")


        names = ["RElbowRoll","RElbowYaw", "RWristYaw", "RShoulderPitch", "RShoulderRoll"]
        angles = [1.46654,0.05211,1.60452, 0.17951, -0.25315]
        fractionMaxSpeed = 0.2
        motionProxy.setAngles(names, angles, fractionMaxSpeed)
        time.sleep(2);


        effector   = "RArm"
        space      = motion.FRAME_ROBOT
        path      = [
            [0.00, 0.00, +0.00, 0.0, 0.0, 0.0],    # N1
            [0.03, 0.00, +0.00, 0.0, 0.0, 0.0],    # N2
            [0.0, -0.02, +0.00, 0.0, 0.0, 0.0],    # N3
            [+0.03, -0.02, +0.00, 0.0, 0.0, 0.0],  # N4
            [0.00, -0.03, +0.10, 0.0, 0.0, 0.0],   # MEP new point
            [0.00, -0.03, +0.00, 0.0, 0.0, 0.0],   # A1
            [+0.04, -0.04, +0.00, 0.0, 0.0, 0.0],  # A2
            [-0.001, -0.05, +0.00, 0.0, 0.0, 0.0],    # A3
            [0.00, -0.06, +0.10, 0.0, 0.0, 0.0],   # MEP new point
            [0.00, -0.06, +0.00, 0.0, 0.0, 0.0],   # O1
            [0.03, -0.06, +0.00, 0.0, 0.0, 0.0],   # O2
            [0.03, -0.08, 0.0,  0.00,  0.0, 0.0],  # O3
            [0.00, -0.08, +0.00, 0.0, 0.0, 0.0],   # O4
            [0.00, -0.06, +0.00, 0.0, 0.0, 0.0],   # O1, close the letter
        ]
        axisMask   = 7                              # just control position
        times      = [1.0, 2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0] # seconds
        isAbsolute = False
        motionProxy.positionInterpolation(effector, space, path,axisMask, times, isAbsolute)       # 8 pts
        path0=[  # MEP new point
            [0.00, 0.00, +0.00, 0.0, 0.0, 0.0],    # N1
            [0.02, 0.00, +0.00, 0.0, 0.0, 0.0],    # N2
            [0.0, -0.02, +0.00, 0.0, 0.0, 0.0],    # N3
            [+0.02, -0.02, +0.00, 0.0, 0.0, 0.0],  # N4
        ]
        timezzz     = [1.0,2.0,3.0, 4.0]
        #motionProxy.positionInterpolation(effector, space, path0,axisMask, timezzz, isAbsolute)       # 8 pt
if __name__ == "__main__":
    robotIp = config.ipnao

    print "Usage python WriteNao.py on nao.local"

    main(robotIp)
