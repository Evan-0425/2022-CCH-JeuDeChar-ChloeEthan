#!/usr/bin/python
import multiprocessing
import sys
import time
import brickpi3

import deplacement

# Brickpi
BP = brickpi3.BrickPi3()

# Déclaration des variables de capteurs de la brique
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.TOUCH)

# Fonction principale lancée sur un thread
def main():
   deplacement.deplacement()
   print("j'ai fini")

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
processPrincipal = multiprocessing.Process(target=main)
processPrincipal.start()

processBouton = multiprocessing.Process(target=arretBouton)
processBouton.start()
