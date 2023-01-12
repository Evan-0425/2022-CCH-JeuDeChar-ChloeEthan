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

# Définitions des vitesses et limites de moteurs
BP.set_motor_limits(BP.PORT_A, 300, 300)
BP.set_motor_limits(BP.PORT_B, 80, 80)
BP.set_motor_limits(BP.PORT_C, 80, 450)
BP.set_motor_limits(BP.PORT_D, 300, 300)

BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))


# Stop le programme après clique sur le bouton
def stopAllMotors():
    BP.set_motor_position(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))  # Ouverture de la pince
    BP.set_motor_position(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))  # Véhicule
    BP.set_motor_position(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))  # Descendre / Monter pince
    BP.set_motor_position(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))  # Plateforme


def arretBouton():
    while True:
        etatBouton = 0
        try:
            etatBouton = BP.get_sensor(BP.PORT_3)
            print(etatBouton)
            time.sleep(0.05)
        except:
            print("erreur de prise de mesure")

        if etatBouton == 1:
            stopAllMotors()
            os._exit(1)


# Lancement du thread pour le bouton
processBouton = Thread(target=arretBouton)
processBouton.start()

# Main
print("je lance")
BP.set_motor_position(BP.PORT_D, 2000)  # Plateforme
