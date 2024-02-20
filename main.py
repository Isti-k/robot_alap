#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
#motorok kezelése
jm = Motor(Port.B)
bm = Motor(Port.C)
robot = DriveBase(jm, bm, 56, 132)

#szenzorok
us = UltrasonicSensor(Port.S4)
ts = TouchSensor(Port.S1)
cs = ColorSensor(Port.S3)

#vár
wait(700)

#satufék
robot.stop(Stop.BRAKE)

#robot irányítása
robot.drive(400,0)
wait(700)


#fordul 90 fokot
robot.drive(0,180)
wait(700)

robot.drive(-400,0)
wait(700)



# Write your program here.
ev3.speaker.beep()