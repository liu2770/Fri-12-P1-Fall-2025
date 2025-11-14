# !/usr/bin/env python3
# coding: utf-8
# --------------------------------------------------------------------------------

import sys  #TODO: CHECK THE STYLING AND FUNCTION NAMES

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
##Functions
def gripperInit():  #Initialize gripper state

    arm.home()
    sleep(1)

    close_gripper()
    sleep(1)
    return

def open_gripper(degree):

    arm.rotate_gripper(-degree)
    sleep(1)
    return

def close_gripper():

    arm.rotate_gripper(720)
    sleep(1)
    return

def move_to_parcel():

    #TODO: Store the script for moving the gripper to parcel location
    return

def target_1_logic():   #Sponge

    #TODO: Store the script for picking up object 1 and return to home

    arm.home()
    sleep(1)
    open_gripper(20)
    sleep(1)
    arm.rotate_base(15)
    arm.get_arm_position()
    sleep(1)
    arm.rotate_elbow(-10)
    sleep(1)
    arm.rotate_shoulder(45)

    close_gripper()

    arm.rotate_shoulder(-45)

    arm.home()
    return

def target_2_logic():   #Bottel

    #TODO: Store the script for picking up object 2 and return to home

    arm.home()
    sleep(1)
    open_gripper(30)
    sleep(1)
    arm.rotate_base(8)
    sleep(1)
    arm.rotate_elbow(-17)
    sleep(1)
    arm.rotate_shoulder(50)
    sleep(1)

    close_gripper()

    arm.rotate_shoulder(-45)

    arm.home()
    sleep(1)
    return

def target_3_logic():   #D12

    #TODO: Store the script for picking up object 3 and return to home

    arm.home()
    sleep(1)
    return

def target_4_logic():   #Wizard hat

    #TODO: Store the script for picking up object 4 and return to home

    arm.home()
    sleep(1)
    arm.rotate_base(-3)
    sleep(1)
    arm.rotate_elbow(-5)
    sleep(1)
    arm.rotate_shoulder(40)
    sleep(1)
    print(f"Rook position: {arm.get_arm_position()}")
    return

def target_5_logic():   #Bowl

    #TODO: Store the script for picking up object 5 and return to home

    arm.home()
    sleep(1)
    return

def target_6_logic():   #Rook

    arm.home()
    sleep(1)

    arm.rotate_base(3)
    sleep(1)
    arm.rotate_elbow(-5)
    sleep(1)
    arm.rotate_shoulder(40)
    #arm.set_arm_position([0.5563790264878321, 0.028623598527956644, 0.1451919543714052]
    print(f"Rook position: {arm.get_arm_position()}")
    sleep(1)
    return

##Testing starts here

#init
gripperInit()
#list=scan_barcode().split()
#print(list)
#target_1_logic()
target_4_logic()

#TODO: get arm to one of the objects
#TODO: try get the scooper to go below the object
#TODO: squeez the object with the grippers
#TODO: test if the gripper can rotate 180 so the object kidna rest on the scooper

#print useful data
#print(arm.get_arm_position())

#TODO: get the arm to the percel loc
#TODO: drop the object
#TODO: return to initial position, ready to repeate above process if needed!!!


# ---------------------------------------------------------------------------------
# STUDENT CODE ENDS
# ---------------------------------------------------------------------------------

arm.end_arm_connection()