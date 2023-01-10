#!/usr/bin/python
import multiprocessing
import sys

import time
import brickpi3

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.TOUCH)

def print_time(threadName, counter, delay):
   print("je suis dans l'affichage de temps")
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

def arretBouton():
   while True:
      etatBouton = 0
      try:
         etatBouton = BP.get_sensor(BP.PORT_3)
         print(etatBouton)
         time.sleep(0.1)
      except:
         print("erreur de prise de mesure")

      if etatBouton == 1:
         processPrincipal.terminate()
         sys.exit()


processPrincipal = multiprocessing.Process(target=print_time, args=("Thread 1", 1000, 0.1))
processPrincipal.start()

processBouton = multiprocessing.Process(target=arretBouton())
processBouton.start()


