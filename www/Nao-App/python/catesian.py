# -*- encoding: UTF-8 -*-

'''Cartesian control: Arm trajectory example'''

import sys
import motion
import time
import config
from naoqi import ALProxy


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(robotIP):
    ''' Example showing a hand ellipsoid
    Warning: Needs a PoseInit before executing
    '''

    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)
    #postureProxy.goToPosture("crouch", 0.5)
    names = ["RElbowYaw", "RWristYaw", "RShoulderPitch", "RShoulderRoll"]
    angles = [0.21318,1.54776, 0.15190, -0.04146]
    fractionMaxSpeed = 0.2
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(2);

    effector= "RArm"
    space = motion.FRAME_ROBOT
    path = [
        [0.1, -0.15, +0.00, 0.0, 0.0, 0.0],  # point 1
        [-0.1, +0.00, +0.00, 0.0, 0.0, 0.0],
        [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]]
    axisMask = 7  # just control position
    times = [2.0,4.0,6.0]  # seconds
    isAbsolute = False
    motionProxy.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)


if __name__ == "__main__":
    robotIp = config.ipnao
    print "Usage python cathesian.py nao.local"
    main(robotIp)
