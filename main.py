#!/usr/bin/python
import multiprocessing
import sys
import time
import brickpi3

import deplacement

# Brickpi
BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.TOUCH)

# Fonction principale lancée sur un thread
def main(counter, delay):
   deplacement.deplacement()
   print("je suis dans l'affichage de temps")
   while counter:
      time.sleep(delay)
      print ("%s: %s" + time.ctime(time.time()))
      counter -= 1

# Stop le programme après clique sur le bouton
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


# Lancement des deux threads
processPrincipal = multiprocessing.Process(target=main, args=("Thread 1", 1000, 0.1))
processPrincipal.start()

processBouton = multiprocessing.Process(target=arretBouton())
processBouton.start()


