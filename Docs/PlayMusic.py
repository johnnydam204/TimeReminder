import os
import glob
import subprocess
from time import sleep
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(22,GPIO.IN)   # pin 15
#GPIO.setup(23,GPIO.IN)   # pin 16
#GPIO.setup(24,GPIO.IN)   # pin 18
#GPIO.setup(25,GPIO.IN)   # pin 22

sleep(20)
os.chdir('/media/pi/CF88-EAC8/mp3')
f = glob.glob('*.mp3')
#print f
h = len(f)
flag=1
pt=0
st=0

#while True:
#    if flag==1:
#        player = subprocess.Popen(["omxplayer -o local",f[pt]],stdin=subprocess.PIPE) #,stdout=subprocess.PIPE,stderr=subprocess.PIPE
#        fi = player.poll()
#        flag=0
#        st=0

os.system("omxplayer -o local /media/pi/CF88-EAC8/mp3/Track01.mp3 &")

   sleep(0.1)

    
#player.stdin.write("+")

#player.stdin.write("-")