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
#     arm.rotate_base(-47)
#     sleep(1)
#     arm.rotate_elbow(40)
#     sleep(1)
#     open_gripper(40)
    arm.set_arm_position([0.22503238356190008, -0.23900971615063057, 0.22808881742811488])
    open_gripper(40)
    return

def target_1_logic():   #Sponge

    #TODO: Store the script for picking up object 1 and return to home

#     arm.home()
#     sleep(1)
#     open_gripper(30)
#     sleep(1)
#     arm.rotate_base(14)
#     sleep(1)
#     arm.rotate_elbow(-9)
#     sleep(1)
#     arm.rotate_shoulder(45)
#     sleep(1)
#     arm.get_arm_position()
#     #arm.set_arm_position([0.550975716856366, 0.13490690429229635, 0.08579730620303272])
#
#     close_gripper()
#
#     arm.rotate_shoulder(-45)

#     arm.home()


#     arm.home()
#     sleep(1)
#     open_gripper(23)
#     sleep(1)
#     arm.rotate_base(16.5)
#     sleep(1)
#     arm.rotate_elbow(-10)
#     sleep(1)
#     arm.rotate_shoulder(35)
#     sleep(1)
#     arm.get_arm_position()
    open_gripper(20)
    sleep(1)
    arm.set_arm_position([0.5490539443478295, 0.15789464150191637, 0.19156143380856633])
    sleep(1)
    arm.rotate_shoulder(5)
    sleep(1)
    arm.rotate_elbow(-2)
    sleep(1)
    close_gripper()
    sleep(1)
    arm.rotate_shoulder(-45)

    move_to_parcel()

    arm.home()
    return

def target_2_logic():   #Bottle

    #TODO: Store the script for picking up object 2 and return to home

    arm.home()
    sleep(1)
    open_gripper(15)
    sleep(1)
    arm.rotate_base(8)
    sleep(1)
    arm.rotate_elbow(-16)
    sleep(1)
    arm.rotate_shoulder(52)
    sleep(1)
    arm.get_arm_position()
#     open_gripper(15)
#     arm.set_arm_position([0.5850203821304305, 0.07719062354168196, 0.05075644615654784])

    close_gripper()

    arm.rotate_shoulder(-45)

    move_to_parcel()

    arm.home()
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

#     open_gripper(15)
#     sleep(1)
#     arm.rotate_base(2)
#     sleep(1)
#     arm.rotate_elbow(-10)
#     sleep(1)
#     arm.rotate_shoulder(48)
#     arm.get_arm_position()
    open_gripper(15)
    arm.set_arm_position([0.5714053048456229, 0.01622402562232702, 0.08827264038887025])
    sleep(1)

    close_gripper()

    arm.rotate_shoulder(-50)
    sleep(1)

    move_to_parcel()
    return

##Testing starts here

#init
gripperInit()
#list=scan_barcode().split()
#print(list)
#move_to_parcel()
target_1_logic()
#arm.home()


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