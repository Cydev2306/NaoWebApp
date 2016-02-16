from naoqi import *
from vision_definitions import *
from cv2 import *
from numpy import *
import config
naoIP = config.ipnao
moduleName="OpenCVDemo"
camera = 0 # 1 = bas / 0 = haut

#creer un proxy vers le module ALVideoDevice
videoProxy =ALProxy("ALVideoDevice",naoIP,9559)
# specifier au module type d'image
try:
	while(True):
		videoProxy.unsubscribe(moduleName)
except:
	pass
moduleName =videoProxy.subscribeCamera(moduleName,camera,kVGA,kBGRColorSpace,30)
#obtenir une image
ImageNAO = videoProxy.getImageRemote(moduleName)

# lire les parametres
largeur = ImageNAO[0]
hauteur = ImageNAO[1]
canaux  = ImageNAO[2]
imageBrute = ImageNAO[6]
# Conversion magique  vers OpenCV
imageBGR = fromstring(imageBrute, dtype="uint8").reshape(hauteur, largeur, canaux)
# affichage de l image originale
imshow("Camera", imageBGR)
waitKey()
videoProxy.unsubscribe(moduleName)
