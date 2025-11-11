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
#TODO: Redo the skeletal strcuture, keywords: open&close, individual functions for all objects, move to parcel from home
##Global variables
action_interval=1   #time in seconds
##Functions
def gripperInit():  #Initialize gripper state
    arm.home()
    sleep(action_interval)

    close_gripper()
    sleep(action_interval)
    return

def open_gripper():
    arm.rotate_gripper(-120)
    sleep(action_interval)
    return

def close_gripper():
    arm.rotate_gripper(120)
    sleep(action_interval)
    return

def move_to_parcel():
    #TODO: Store the script for moving the gripper to parcel location
    return

def target_1_logic():   #Sponge
    #TODO: Store the script for picking up object 1 and return to home

    arm.home()
    sleep(action_interval)
    return

def target_2_logic():   #Bottel
    #TODO: Store the script for picking up object 2 and return to home

    arm.home()
    sleep(action_interval)
    return

def target_3_logic():   #D12
    #TODO: Store the script for picking up object 3 and return to home

    arm.home()
    sleep(action_interval)
    return

def target_4_logic():   #Wizard hat
    #TODO: Store the script for picking up object 4 and return to home

    arm.home()
    sleep(action_interval)
    return

def target_5_logic():   #Bowl
    #TODO: Store the script for picking up object 5 and return to home

    arm.home()
    sleep(action_interval)
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