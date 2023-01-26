#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3

from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division

import brickpi3  # import the BrickPi3 drivers
import time

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_3,BP.SENSOR_TYPE.TOUCH)  # Configure for a touch sensor. If an EV3 touch sensor is connected, it will be configured for EV3 touch, otherwise it'll configured for NXT touch.
A       = 1020  #Degrés
B       = 1650  #Degrés
C       = 2200  #Degrés
D       = 2645  #Degrés
E       = 3050  #Degrés
F       = 3620  #Degrés
G       = 4250  #Degrés
UN      = -20   #Degré
DEUX    = -165  #Degrés
TROIS   = -280  #Degrés
QUATRE  = -375  #Degrés
CINQ    = -465  #Degrés
SIX     = -550  #Degrés
SEPT    = -730  #Degrés

#              Coordonnées des points du jeu                                  PORT_D                                 PORT_B
#
#            G1-------------D1-------------A1  X                X  à  A   ->  1020°                 1  à  1   ->      -20°
#            |              |               |                      à  B   ->  1650°                    à  2   ->     -165°
#            |    F2--------D2--------B2    |                      à  C   ->  2200°                    à  3   ->     -280°
#            |    |         |         |     |                      à  D   ->  2645°                    à  4   ->     -375°
#            |    |    E3---D3---C3   |     |                      à  E   ->  3050°                    à  5   ->     -465°
#            |    |    |          |   |     |                      à  F   ->  3620°                    à  6   ->     -550°
#            G4---F4---E4        C4---B4---A4                      à  G   ->  4250°                    à  7   ->     -730°
#            |    |    |          |   |     |
#            |    |    E5---D5---C5   |     |
#            |    |         |         |     |
#            |    F6--------D6--------B6    |
#            |              |               |
#            G7-------------D7-------------A7
#

def deplacementCoordonne(coLettre, coChiffre):
    BP.set_motor_position(BP.PORT_B, coChiffre)
    BP.set_motor_position(BP.PORT_D, coLettre)

# Fonction en lien avec la pince
def resetPlier():
    closePlier()
    upPlier()

def openPlier():
    BP.set_motor_position(BP.PORT_A, 350)
    time.sleep(0.3)
def downPlier():
    BP.set_motor_position(BP.PORT_C, 1850)

def closePlierPion():
    BP.set_motor_position(BP.PORT_A, 130)
def closePlier():

    nouveauDegreMoteur = BP.get_motor_encoder(BP.PORT_A)
    degreMoteur = 1631731787
    BP.set_motor_power(BP.PORT_A, -50)
    time.sleep(0.1)

    while nouveauDegreMoteur != degreMoteur:

        degreMoteur = nouveauDegreMoteur
        time.sleep(0.2)
        nouveauDegreMoteur = BP.get_motor_encoder(BP.PORT_A)
        print("Ancien degré : ", str(degreMoteur), "°\t Nouveau degré : ", str(nouveauDegreMoteur), "°")

    time.sleep(1.0)
    BP.set_motor_power(BP.PORT_A, 0)
    nouveauDegreMoteur += 150
    print("\nDegré objectif : ", str(nouveauDegreMoteur) ,"°")
    BP.set_motor_position(BP.PORT_A, nouveauDegreMoteur)
    time.sleep(2.0)
    print("Degré actuel : ", BP.get_motor_encoder(BP.PORT_A), "°\n")

def upPlier():

    nouveauDegreMoteur = BP.get_motor_encoder(BP.PORT_C)
    degreMoteur = 823432432
    BP.set_motor_power(BP.PORT_C, -50)
    time.sleep(0.1)

    while nouveauDegreMoteur != degreMoteur:

        degreMoteur = nouveauDegreMoteur
        time.sleep(0.2)
        nouveauDegreMoteur = BP.get_motor_encoder(BP.PORT_C)
        print("Ancien degré : ", str(degreMoteur), "°\t Nouveau degré : ", str(nouveauDegreMoteur), "°")

    time.sleep(1.0)
    BP.set_motor_power(BP.PORT_C, 0)
    nouveauDegreMoteur += 60
    print("\nDegré objectif : ", str(nouveauDegreMoteur), "°")
    BP.set_motor_position(BP.PORT_C, nouveauDegreMoteur)
    time.sleep(2.0)
    print("Degré actuel : ", BP.get_motor_encoder(BP.PORT_C), "°\n")

def recupPion():
    downPlier()
    time.sleep(10.0)
    closePlierPion()
    time.sleep(4.0)
    upPlier()
    time.sleep(3.0)

try:
    try:

        BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
        BP.set_motor_limits(BP.PORT_A, 300, 200)
        BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
        BP.set_motor_limits(BP.PORT_C, 80, 250)
        resetPlier()
        time.sleep(4.0)

        BP.reset_motor_encoder(BP.PORT_A)
        BP.reset_motor_encoder(BP.PORT_C)
        BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
        BP.set_motor_limits(BP.PORT_A, 300, 200)
        BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
        BP.set_motor_limits(BP.PORT_B, 80, 80)
        BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
        BP.set_motor_limits(BP.PORT_C, 80, 250)
        BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
        BP.set_motor_limits(BP.PORT_D, 80, 300)




    except IOError as error:
        print(error)

    openPlier()
    deplacementCoordonne(A, SEPT)
    time.sleep(15.0)

    recupPion()
    BP.set_motor_position(BP.PORT_B, 0)
    BP.set_motor_position(BP.PORT_D, 0)

except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.

print("A ton tour !")
