#!/usr/bin/python
import multiprocessing
import sys
import time
import brickpi3
import os
from threading import Thread

# Brickpi
BP = brickpi3.BrickPi3()

# Déclaration des variables de capteurs de la brique
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.TOUCH)

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
         os._exit(1)

# Lancement du thread pour le bouton
processBouton = Thread(target=arretBouton)
processBouton.start()

# Main
while True:
   time.sleep(0.1)
   print("Je suis dans la boucle")