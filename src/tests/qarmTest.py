"""
Script for testing the Q arm, NOT a part of the actual program
Fri-12 P1, Jincheng Liu, 2025 Fall
"""
# !/usr/bin/env python3
# coding: utf-8
# --------------------------------------------------------------------------------

import sys

sys.path.append("../")

from time import sleep
from Common.qarm_interface_wrapper import *

GRIPPER_IMPLEMENTATION = 1
arm = QArmInterface(GRIPPER_IMPLEMENTATION)
scan_barcode = BarcodeScanner.scan_barcode

# --------------------------------------------------------------------------------
# STUDENT CODE BEGINS
# ---------------------------------------------------------------------------------

##Global variables
motorStepsTotal=0 #Used to restore the system to its original state at the end of the program

##Functions
def motorAction(deg):
    """
    Encapsulation of some sort, should be called instead all time whenever arm.rotate_gripper() is needed.
    Records the steps of the motor then rotate the gripper.
    """
    motorStepsTotal+deg
    arm.rotate_gripper(deg)
    return

def target_1_logic():
    #TODO: Store the scipt for picking up and dropping object 1
    return

##Testing starts here

#init
arm.home()

#TODO: get arm to one of the objects
#TODO: try get the scooper to go below the object
#TODO: squeez the object with the grippers
#TODO: test if the gripper can rotate 180 so the object kidna rest on the scooper

#print useful data
print(arm.get_arm_position())

#TODO: get the arm to the percel loc
#TODO: drop the object
#TODO: return to initial position, ready to repeate above process if needed!!!


# ---------------------------------------------------------------------------------
# STUDENT CODE ENDS
# ---------------------------------------------------------------------------------

arm.end_arm_connection()