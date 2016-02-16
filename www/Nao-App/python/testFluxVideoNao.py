import cv2
import vision_definitions
from naoqi import *
import config


proxyVideo = ALProxy("ALVideoDevice",config.ipnao, 9559)

resolution = vision_definitions.kQVGA  # 320 * 240
colorSpace = vision_definitions.kRGBColorSpace
print proxyVideo.subscribeCamera("nao",1,resolution,colorSpace, 15)
#cap = cv2.VideoCapture(0)

#while True:
#    ret,im = cap.read()
#    cv2.imshow('videoTest',im)
#    key = cv2.waitKey(10)
