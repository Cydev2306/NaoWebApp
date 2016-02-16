import sys
import datetime
import time
import config
from naoqi import ALProxy

import Image

def miniature(IP, PORT, nomVideo):
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
  im.save("../public/videoNao/miniature/"+nomVideo+".jpeg", "JPEG")


if __name__ == "__main__":
    IP = config.ipnao  # Replace here with your NaoQi's IP address.
    PORT = 9559
    nomVideo = time.strftime('%d-%m-%y_a_%H-%M-%S',time.localtime())
    #Take a photo to make a miniature
    naoImage = miniature(IP, PORT, nomVideo)

    # Read IP address from first argument if any.
    if len(sys.argv) > 1:
        IP = sys.argv[1]

    videoRecorderProxy = ALProxy("ALVideoRecorder", IP, PORT)

    # This records a 320*240 MJPG video at 10 fps.
    # Note MJPG can't be recorded with a framerate lower than 3 fps.
    videoRecorderProxy.setResolution(1)
    videoRecorderProxy.setFrameRate(10)
    videoRecorderProxy.setVideoFormat("MJPG")
    videoRecorderProxy.startRecording("/var/www/Nao-App/public/cameras", "record")

    time.sleep(5)

    # Video file is saved on the robot in the
    # /home/nao/recordings/cameras/ folder.
    videoInfo = videoRecorderProxy.stopRecording()

    print "Video was saved on the robot: ", videoInfo[1]
    print "Num frames: ", videoInfo[0]

    print nomVideo
