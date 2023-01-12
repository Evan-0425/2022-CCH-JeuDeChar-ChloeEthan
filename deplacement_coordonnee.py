#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3

from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division

import brickpi3  # import the BrickPi3 drivers
import time

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_3,BP.SENSOR_TYPE.TOUCH)  # Configure for a touch sensor. If an EV3 touch sensor is connected, it will be configured for EV3 touch, otherwise it'll configured for NXT touch.
A = 1020
B = 1650
C = 2200
D = 2645
E = 3050
F = 3620
G = 4210
UN = 0
DEUX = -135
TROIS = -280
QUATRE = -375
CINQ = -465
SIX = -550
SEPT = -700

#              Coordonnées des points du jeu
#
#            G1-------------D1-------------A1
#            |              |               |
#            |    F2--------D2--------B2    |
#            |    |         |         |     |
#            |    |    E3---D3---C3   |     |
#            |    |    |          |   |     |
#            G4---F4---E4        C4---B4---A4
#            |    |    |          |   |     |
#            |    |    E5---D5---C5   |     |
#            |    |         |         |     |
#            |    F6--------D6--------B6    |
#            |              |               |
#            G7-------------D7-------------A7
#



try:
    try:
        BP.set_motor_position(BP.PORT_A, 10)
        time.sleep(1.0)

        BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
        BP.set_motor_limits(BP.PORT_A, 300, 300)
        BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
        BP.set_motor_limits(BP.PORT_B, 80, 80)
        BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
        BP.set_motor_limits(BP.PORT_C, 80, 450)
        BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
        BP.set_motor_limits(BP.PORT_D, 300, 300)

    except IOError as error:
        print(error)

    def deplacementCoordonne(coLettre, coChiffre):
        BP.set_motor_position(BP.PORT_B, coChiffre)
        BP.set_motor_position(BP.PORT_D, coLettre)
        BP.set_motor_position(BP.PORT_A, 380)  # Pince (ouvert/fermé)

    def resetPince():
        BP.set_motor_position(BP.PORT_A, 20)
        BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))

    def bougeMoteur(nomPort, degre):

        BP.set_motor_position(nomPort, degre)
        nouveauDegreMoteur = BP.get_motor_encoder(nomPort)

        while nouveauDegreMoteur != degre:
            time.sleep(0.1)
            degreMoteur = nouveauDegreMoteur
            nouveauDegreMoteur = BP.get_motor_encoder(nomPort)

            if nouveauDegreMoteur == degreMoteur:
                BP.set_motor_position(nomPort, BP.get_motor_encoder(nomPort))
                BP.set_motor_position(nomPort, 30)
                return


    deplacementCoordonne(D, TROIS)

    time.sleep(15.0)
    BP.set_motor_position(BP.PORT_C, 1875)  # pince (haut/bas)
    time.sleep(5.0)
    BP.set_motor_position(BP.PORT_A, 180)   # Ferme la pince
    time.sleep(4.00)
    BP.set_motor_position(BP.PORT_C, 10)
    time.sleep(3.0)
    BP.set_motor_position(BP.PORT_B, 0)
    BP.set_motor_position(BP.PORT_D, 0)

except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.


