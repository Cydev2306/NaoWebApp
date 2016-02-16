# -*- encoding: UTF-8 -*-
# Get an image from NAO. Display it and save it using PIL.

import sys
import datetime
import time
import threading
import config
# Python Image Library
from PIL import Image

from naoqi import ALProxy


def showNaoImage(IP, PORT):
  camProxy = ALProxy("ALVideoDevice", IP, PORT)
  resolution = 2    # VGA
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  # Get a camera image.
  # image[6] contains the image data passed as an array of ASCII chars.
  naoImage = camProxy.getImageRemote(videoClient)

  camProxy.unsubscribe(videoClient)


  # Now we work with the image returned and save it as a PNG  using ImageDraw
  # package.

  # Get the image size and pixel array.
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  # Create a PIL Image from our pixel array.
  im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

  # Save the image.
  im.save("../public/imgNao/live.jpeg", "JPEG")


def main(IP,PORT,post):
	if post == True:
		print "post = true"
	else:
		print "poste = false"
	while post == True :
		naoImage = showNaoImage(IP, PORT)
		print "photo"


if __name__ == '__main__':
  IP = config.ipnao
  PORT = 9559

  if len(sys.argv) > 1:
	  if(sys.argv[1] == "True"):
		  post = True
	  else:
		  post = False
	  main(IP,PORT,post)
	 # a = threading.Thread(None, main, None, , None)
	 # if(post == True):
		#  a.start()
	  #else:
	#	  a._Thread__stop()
