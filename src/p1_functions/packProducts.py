# !/usr/bin/env python3
# coding: utf-8
# --------------------------------------------------------------------------------

import sys

sys.path.append("../")

from time import sleep
from Common.qarm_interface_wrapper import *

def pack_logic_handler(arm,item):
    gripperInit(arm)
    match item:
        case "Sponge":
            target_1_logic(arm)
            pass
        case "Bottle":
            target_2_logic(arm)
            pass
        case "D12":
            target_3_logic(arm)
            pass
        case "Rook":
            target_6_logic(arm)
            pass
        case "WitchHat":
            target_4_logic(arm)
            pass
        case "Bowl":
            target_5_logic(arm)
            pass
    return


def pack_products(product_list):
    GRIPPER_IMPLEMENTATION = 1
    arm = QArmInterface(GRIPPER_IMPLEMENTATION)

    for product in product_list:
        pack_logic_handler(arm,product[0])
        print(f"{product[0]} has been packed")

    print("All items packed successfully")

    arm.end_arm_connection()
    return

def gripperInit(arm):  #Initialize gripper state

    arm.home()
    sleep(1)

    close_gripper()
    sleep(1)
    return

def open_gripper(arm,degree):

    arm.rotate_gripper(-degree)
    sleep(1)
    return

def close_gripper(arm):

    arm.rotate_gripper(720)
    sleep(1)
    return

def move_to_parcel(arm):
    arm.set_arm_position([0.22503238356190008, -0.23900971615063057, 0.22808881742811488])
    open_gripper(arm,40)
    return

def target_1_logic(arm):   #Sponge
    open_gripper(arm,20)
    sleep(1)
    arm.set_arm_position([0.5490539443478295, 0.15789464150191637, 0.19156143380856633])    #Get Q-arm to the space above the obect
    sleep(1)
    
    arm.rotate_shoulder(5)  #Final Descend to grab the object
    sleep(1)
    arm.rotate_elbow(-2)
    sleep(1)
    close_gripper(arm)
    sleep(1)

    arm.rotate_shoulder(-45)    #Bring the Q-arm up
    sleep(1)

    move_to_parcel(arm)

    arm.home()
    return

def target_2_logic(arm):   #Bottle

    open_gripper(15)
    arm.set_arm_position([0.5850203821304305, 0.07719062354168196, 0.05075644615654784])
    sleep(1)

    close_gripper()
    sleep(1)

    arm.rotate_shoulder(-45)
    sleep(1)

    move_to_parcel()

    arm.home()
    return

def target_6_logic(arm):   #Rook
    open_gripper(15)
    arm.set_arm_position([0.5714053048456229, 0.01622402562232702, 0.08827264038887025])
    sleep(1)

    close_gripper()
    sleep(1)

    arm.rotate_shoulder(-50)
    sleep(1)

    move_to_parcel()
    return

def target_3_logic(arm):   #D12
    open_gripper(15)
    arm.set_arm_position([0.5694053048456229, -0.01622402562232702, 0.08827264038887025])
    sleep(1)

    close_gripper()
    sleep(1)

    arm.rotate_shoulder(-45)
    sleep(1)

    move_to_parcel()
    return

def target_4_logic(arm):   #Wizard hat
    open_gripper(15)
    arm.set_arm_position([0.5754053048456229, -0.07422402562232702, 0.09127264038887025])
    sleep(1)

    close_gripper()
    sleep(1)

    arm.rotate_shoulder(-45)
    sleep(1)

    move_to_parcel()
    return

def target_5_logic(arm):   #Bowl
    open_gripper(15)
    arm.set_arm_position([0.5604053048456229, -0.15789464150191637, 0.08527264038887025])
    sleep(1)

    close_gripper()
    sleep(1)

    arm.rotate_shoulder(-50)
    sleep(1)

    move_to_parcel()
    return
