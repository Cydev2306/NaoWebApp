# -*- encoding: UTF-8 -*-

import sys
import time
import config
import motion
from naoqi import ALProxy


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
    print proxy.getSummary()

def StiffnessOff(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 0.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

    # print motion state
    print proxy.getSummary()

def ActionSit(motionProxy, postureProxy, vitesse, post=False):
    StiffnessOn(motionProxy)
    if post == True:
        postureProxy.post.goToPosture("Sit", vitesse)
    else:
        postureProxy.goToPosture("Sit", vitesse)
    StiffnessOff(motionProxy)

def ActionCrouch(motionProxy, postureProxy, vitesse):
    ActionStand(motionProxy, postureProxy, vitesse)
    postureProxy.goToPosture("Crouch", vitesse)
    StiffnessOff(motionProxy)

def ActionLyingBack(motionProxy, postureProxy, vitesse, post=False):
    StiffnessOn(motionProxy)
    if post == True:
        postureProxy.post.goToPosture("LyingBack", vitesse)
    else:
        postureProxy.goToPosture("LyingBack", vitesse)
    StiffnessOff(motionProxy)

def ActionLyingBelly(motionProxy, postureProxy, vitesse, post=False):
    StiffnessOn(motionProxy)
    if post == True:
        postureProxy.post.goToPosture("LyingBelly", vitesse)
    else:
        postureProxy.goToPosture("LyingBelly", vitesse)
    StiffnessOff(motionProxy)

def ActionSitRelax(motionProxy, postureProxy, vitesse, post=False):
    StiffnessOn(motionProxy)
    if post == True:
        postureProxy.post.goToPosture("SitRelax", vitesse)
    else:
        postureProxy.goToPosture("SitRelax", vitesse)
    StiffnessOff(motionProxy)

def ActionStandInit(motionProxy, postureProxy, vitesse, post=False):
    StiffnessOn(motionProxy)
    if post == True:
        postureProxy.post.goToPosture("SitInit", vitesse)
    else:
        postureProxy.goToPosture("SitInit", vitesse)

def ActionStandZero(motionProxy, postureProxy, vitesse, post=False):
    StiffnessOn(motionProxy)
    if post == True:
        postureProxy.post.goToPosture("StandZero", vitesse)
    else:
        postureProxy.goToPosture("StandZero", vitesse)
    print motionProxy.getSummary()

def ActionStand(motionProxy, postureProxy, vitesse, post=False):
    StiffnessOn(motionProxy)
    if post == True:
        postureProxy.post.goToPosture("Stand", vitesse)
    else:
        postureProxy.goToPosture("Stand", vitesse)

def ActionMoveBackward(motionProxy, postureProxy, vitesse, post=False):
    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 1.0)

    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnabled(True, True)
    #~ motionProxy.setWalkArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])

    #TARGET VELOCITY
    X = -0.5
    Y = 0
    Theta = 0.0
    Frequency = 0.2 # low speed
    if post == True:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    else:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def ActionMoveForward(motionProxy, postureProxy, vitesse, post=False):
    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnabled(True, True)
    #~ motionProxy.setWalkArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])

    #TARGET VELOCITY
    X = 1.0
    Y = 0
    Theta = 0.0
    Frequency = 0.2 # low speed
    if post == True:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    else:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def ActionLeft(motionProxy, postureProxy, vitesse, post=False):
    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnabled(True, True)
    #~ motionProxy.setWalkArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])

    #TARGET VELOCITY
    X = 0
    Y = 0.5
    Theta = 0.0
    Frequency = 0.0 # low speed
    if post == True:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    else:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def ActionRight(motionProxy, postureProxy, vitesse, post=False):
    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnabled(True, True)
    #~ motionProxy.setWalkArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])

    #TARGET VELOCITY
    X = 0
    Y = -0.5
    Theta = 0
    Frequency = 0.0 # low speed
    if post == True:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    else:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)


def ActionRotateRight(motionProxy, postureProxy, vitesse, post=False):
    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnabled(True, True)
    #~ motionProxy.setWalkArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])

    #TARGET VELOCITY
    X = 0
    Y = 0
    Theta = -0.2
    Frequency = 0.0 # low speed
    if post == True:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    else:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)


def ActionRotateLeft(motionProxy, postureProxy, vitesse, post=False):
    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnabled(True, True)
    #~ motionProxy.setWalkArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])

    #TARGET VELOCITY
    X = 0
    Y = 0
    Theta = 0.2
    Frequency = 0.0 # low speed
    if post == True:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    else:
        motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def ActionStop(motionProxy, postureProxy):
    X = 0
    Y = 0
    Theta = 0
    Frequency = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    ##killMove() et stopMove() sont des autres fonctions pour le faire arrêter de bouger

def ActionSay(tts, text, speed, post=False):
    if post == True:
        tts.post.say(text)
    else:
        tts.say(text)
def ActionRunPostBehavior(behaviorManagerProxy, name):
    if behaviorManagerProxy.isBehaviorRunning(name):
        behaviorManagerProxy.stopBehavior(name)
    behaviorManagerProxy.post.runBehavior(name)

def ActionRunBehavior(behaviorManagerProxy, name):
    if behaviorManagerProxy.isBehaviorRunning(name):
        behaviorManagerProxy.stopBehavior(name)
    behaviorManagerProxy.runBehavior(name)

def ActionStopBehavior(behaviorManagerProxy):
    behaviorManagerProxy.stopAllBehaviors()


def main(robotIP, cmd, arg1, arg2, arg3):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    try:
        behaviorManagerProxy = ALProxy("ALBehaviorManager", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e


    try:
        tts = ALProxy("ALTextToSpeech", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e


    if cmd == "say":
        ActionSay(tts, arg1, 1.0, True)
    elif cmd == "sit":
        ActionSit(motionProxy, postureProxy, 0.5)
    elif cmd == "stand":
        ActionStand(motionProxy, postureProxy, 0.5)
    elif cmd == "runbehavior":
        ActionRunBehavior(behaviorManagerProxy, arg1)
    elif cmd == "stopbehavior":
        ActionStopBehavior(behaviorManagerProxy)
    elif cmd == "none":
        ActionSay(tts, "Null", 1.0)
    elif cmd == "crouch":
        ActionCrouch(motionProxy, postureProxy, 0.5)
    elif cmd == "forward":
        ActionMoveForward(motionProxy, postureProxy, 0.5)
    elif cmd == "backward":
        ActionMoveBackward(motionProxy, postureProxy, 0.5)
    elif cmd == "lyingbelly":
        ActionLyingBelly(motionProxy, postureProxy, 0.5);
    elif cmd == "lyingback":
        ActionLyingBack(motionProxy, postureProxy, 0.5);
    elif cmd == "stop":
        ActionStop(motionProxy, postureProxy)
    elif cmd == "right":
        ActionRight(motionProxy, postureProxy, 0.5, False)
    elif cmd == "left":
        ActionLeft(motionProxy, postureProxy, 0.5, False)
    elif cmd == "rotateleft":
        ActionRotateLeft(motionProxy, postureProxy, 0.5, False)
    elif cmd == "rotateright":
        ActionRotateRight(motionProxy, postureProxy, 0.5, False)
    elif cmd == "scenario":

        #Scénar pour Michel Billaud

		StiffnessOn(motionProxy)
		#ActionStand(motionProxy, postureProxy, 0.7)
		#ActionMoveForward(motionProxy, postureProxy, 0.3)
		#ActionRunPostBehavior(behaviorManagerProxy, "direBonjour")
		#time.sleep(4)
		#ActionStop(motionProxy, postureProxy)
		#ActionStand(motionProxy, postureProxy, 0.5)
		#ActionRunPostBehavior(behaviorManagerProxy, "headspeak")
		#ActionRunPostBehavior(behaviorManagerProxy, "twinkle")
		#ActionRunPostBehavior(behaviorManagerProxy, "armspeak")
		#tts.say("Nous avons fait connaissance Jeudi dernier à saint quentin. Je m'appelle NAO et Matthieu s'occupe de moi à l'In set.")
		#tts.say("Je me suis entrainé et je vais te faire une petite démo.")
		#ActionStopBehavior(behaviorManagerProxy, "armspeak")
		#ActionStopBehavior(behaviorManagerProxy, "headspeak")
		#ActionRunBehavior(behaviorManagerProxy, "dance")
		#ActionStand(motionProxy, postureProxy, 0.2)
		#ActionRunPostBehavior(behaviorManagerProxy, "headspeak")
		#ActionRunPostBehavior(behaviorManagerProxy, "twinkle")
		#tts.say("Je tiens à te saluer et j'espère que tu me suivras encore, car à Saint-Quentin, avec Pierre André, Xavier Bertran et 				toute l'équipe de l'agence de développement, on va faire de très belles choses.")
		#tts.say("Vive le numérique et vive la robotique! ")
		#ActionStand(motionProxy, postureProxy, 0.2)
		#ActionRunPostBehavior(behaviorManagerProxy, "Haka")
		#ActionRunPostBehavior(behaviorManagerProxy, "direAuRevoir")
		#time.sleep(4)
		#ActionStand(motionProxy, postureProxy, 0.5)

		#Scénar présentation créatis


if __name__ == "__main__":
    robotIp = config.ipnao
    cmd = "null"
    if len(sys.argv) <= 1:
        print "Usage python remoteControle.py robotIP (optional default:169.254.66.118)"
    else:
        cmd = sys.argv[1]
        arg1 = "null"
        arg2 = "null"
        arg3 = "null"


        if len(sys.argv) >= 3:
            arg1 = sys.argv[2]

        if len(sys.argv) >= 4:
            arg2 = sys.argv[3]

        if len(sys.argv) >= 5:
            arg3 = sys.argv[4]

        main(robotIp, cmd, arg1, arg2, arg3)
        try:
            motionProxy = ALProxy("ALMotion", robotIp, 9559)
        except Exception, e:
            print "Could not create proxy to ALMotion"
            print "Error was: ", e

        try:
            postureProxy = ALProxy("ALRobotPosture", robotIp, 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
