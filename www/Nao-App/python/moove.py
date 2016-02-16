# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 0.80000, 1.56000, 2.24000, 2.80000, 3.48000, 4.60000])
keys.append([ 0.29602, -0.17032, -0.34059, -0.05987, -0.19333, -0.01078])

names.append("HeadYaw")
times.append([ 0.80000, 1.56000, 2.24000, 2.80000, 3.48000, 4.60000])
keys.append([ -0.13503, -0.35133, -0.41576, -0.41882, -0.52007, -0.37587])

names.append("LElbowRoll")
times.append([ 0.72000, 1.48000, 2.16000, 2.72000, 3.40000, 4.52000])
keys.append([ -1.37902, -1.29005, -1.18267, -1.24863, -1.31920, -1.18421])

names.append("LElbowYaw")
times.append([ 0.72000, 1.48000, 2.16000, 2.72000, 3.40000, 4.52000])
keys.append([ -0.80386, -0.69188, -0.67960, -0.61057, -0.75324, -0.67040])

names.append("LHand")
times.append([ 1.48000, 4.52000])
keys.append([ 0.00416, 0.00419])

names.append("LShoulderPitch")
times.append([ 0.72000, 1.48000, 2.16000, 2.72000, 3.40000, 4.52000])
keys.append([ 1.11824, 0.92803, 0.94030, 0.86207, 0.89735, 0.84212])

names.append("LShoulderRoll")
times.append([ 0.72000, 1.48000, 2.16000, 2.72000, 3.40000, 4.52000])
keys.append([ 0.36352, 0.22699, 0.20398, 0.21779, 0.24847, 0.22699])

names.append("LWristYaw")
times.append([ 1.48000, 4.52000])
keys.append([ 0.14722, 0.11961])

names.append("RElbowRoll")
times.append([ 0.64000, 1.40000, 1.68000, 2.08000, 2.40000, 2.64000, 3.04000, 3.32000, 3.72000, 4.44000])
keys.append([ 1.38524, 0.24241, 0.34907, 0.93425, 0.68068, 0.19199, 0.26180, 0.70722, 1.01927, 1.26559])

names.append("RElbowYaw")
times.append([ 0.64000, 1.40000, 2.08000, 2.64000, 3.32000, 3.72000, 4.44000])
keys.append([ -0.31298, 0.56447, 0.39113, 0.34818, 0.38192, 0.97738, 0.82678])

names.append("RHand")
times.append([ 1.40000, 3.32000, 4.44000])
keys.append([ 0.01490, 0.01492, 0.00742])

names.append("RShoulderPitch")
times.append([ 0.64000, 1.40000, 2.08000, 2.64000, 3.32000, 4.44000])
keys.append([ 0.24702, -1.17193, -1.08910, -1.26091, -1.14892, 1.02015])

names.append("RShoulderRoll")
times.append([ 0.64000, 1.40000, 2.08000, 2.64000, 3.32000, 4.44000])
keys.append([ -0.24241, -0.95419, -0.46024, -0.96033, -0.32832, -0.25008])

names.append("RWristYaw")
times.append([ 1.40000, 3.32000, 4.44000])
keys.append([ -0.31298, -0.30377, 0.18250])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion","nao.local",9559)
except BaseException, err:
  print err
