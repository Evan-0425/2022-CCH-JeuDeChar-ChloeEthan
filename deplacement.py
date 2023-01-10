#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for running all motors while a touch sensor connected to PORT_1 of the BrickPi3 is being pressed.
#
# Hardware: Connect EV3 or NXT motor(s) to any of the BrickPi3 motor ports. Make sure that the BrickPi3 is running on a 9v power supply.
#
# Results:  When you run this program, the motor(s) speed will ramp up and down while the touch sensor is pressed. The position for each motor will be printed.
from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division

import brickpi3  # import the BrickPi3 drivers
import time

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_3,
                   BP.SENSOR_TYPE.TOUCH)  # Configure for a touch sensor. If an EV3 touch sensor is connected, it will be configured for EV3 touch, otherwise it'll configured for NXT touch.

def deplacement():
    try:
        try:
            BP.set_motor_position(BP.PORT_A, 0)
            time.sleep(3.0)
            BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
            BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
            BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
            BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
            BP.set_motor_limits(BP.PORT_A, 300, 300)
            BP.set_motor_limits(BP.PORT_B, 80, 80)
            BP.set_motor_limits(BP.PORT_C, 80, 450)
            BP.set_motor_limits(BP.PORT_D, 300, 300)
        except IOError as error:
            print(error)
        print("Press touch sensor on port 3 to run motors")
        value = 0

        while not value:
            try:
                value = BP.get_sensor(BP.PORT_3)
            except brickpi3.SensorError:
                pass
            BP.set_motor_position(BP.PORT_D, 1650)  # Plateforme
            BP.set_motor_position(BP.PORT_B, -130)  # Véhicule
            BP.set_motor_position(BP.PORT_A, 650)  # Pince (ouvert/fermé)
        BP.set_motor_position(BP.PORT_C, 2750)  # pince (haut/bas)
        time.sleep(7.50)
        BP.set_motor_position(BP.PORT_A, 250)
        time.sleep(4.00)
        BP.set_motor_position(BP.PORT_B, 0)
        BP.set_motor_position(BP.PORT_C, 0)
        BP.set_motor_position(BP.PORT_D, 0)

    except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
        BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
