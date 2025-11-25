# !/usr/bin/env python3
# coding: utf-8
# --------------------------------------------------------------------------------

"""
The main file for P1 Q-arm program. This version combines
all files into one in case there is issues with loading the
normal file structure.
Fri-12 P1, 2025 Fall
"""
import os
import sys
import csv
import bcrypt
import random
import re

sys.path.append("../")

from time import sleep
# from Common.qarm_interface_wrapper import * #!UNCOMMENT BEFORE DEMO

##*Functions
def sign_up():  #?Changes required
    # ask for user id and clean spaces
    userid = input("Enter a new user ID: ").strip()
    # read existing users
    with open("users.csv", "r", newline="") as f:
        reader = csv.reader(f)
        existing = [row[0] for row in reader]
    if userid in existing:
        print("User ID already exists.")
        return
    while True:
        # clean up extra spaces the user might type
        password = input("Enter password (or type CANCEL): ").strip()
        if password.lower() == "cancel":
            print("Sign-up cancelled.")
            return
        # rules the password has to follow (upper, lower, digit, symbol, length)
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!.@#$%^&*()_\[\]]).{6,}$'
        if re.match(pattern, password):
            break
        else:
            print("Password doesn't meet requirements, try again.")
    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    with open("users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([userid, hashed_pw])

    print("Account created.")

def loadUserEntry(): 
    """
    Helper function, handels read from users.csv. Return 
    a 2D list consists of user names and corresponding 
    passwords.
    Jincheng Liu
    """
    userList=[]
    with open("users.csv",newline="") as file:   #using "with" to better handle file IO (close automatically); csv reader eliminates \r (carriage return) and newline statement removes \n at the end
        csvReader=csv.reader(file)
        for userEntry in csvReader:
            userList.append(userEntry)
    return userList
    
def authenticate():
    """
    Handles the entire login authentication process.
    Asks the user to input their user name and password,
    if they dont have one call sign_up(). Return
    the user name upon successful authentication,
    let them keep trying if not. Reads from users.csv.
    Jincheng Liu
    """
    ##Start of the program
    #Proceed to authenticate the user with a while loop
    while True:
        #Ask the user to input their user name, if they dont have one they should let the program know by putting "-1"
        userName=input("Please enter your user name now, enter -1 if you dont have one; quit() for quit: ").strip()  #?Accepts any string at the moment

        #check if sign_up call is needed
        if userName=="quit()":  #?Exit 1
            input("Sign up canceled. Enter anything to continue...")
            return None #Incase user just want to quit
        if userName=="-1":
            sign_up()
            input("Sign up complete, enter anything to continue...")
            userName=input("Please enter your user name now, enter -1 if you dont have one; quit() for quit: ").strip()
        
        #Load the user entry, incase a new user has been added 
        userList=loadUserEntry()

        #Check if the user name exists
        userExist=False #Default states for userExist and userIndex
        uesrIndex=-1    
        for entry in userList:  #!When there are multiple same user names only the first would be recognized
            if entry[0]==userName:
                userExist=True
                uesrIndex=userList.index(entry)

        if userExist==True:
            password=input("User found, please input password now: ").strip()
            expectedPassword=str(userList[uesrIndex][1])    #The str constrcutor doesn't do anything really, it's just here for readability
            if bcrypt.checkpw(password.encode('utf-8'),expectedPassword.encode('utf-8')):    #?Exit2
                print(f"User authentication acknowledged, welcome {userName}.")
                return userName
            else:
                input("Password does not match, enter anything to try again...\n")    #use input to pause the program so user can read the output
        else:
            input("User not found, enter anything to try again...")

def lookup_products(products):  #?Latest
    '''Returns a 2D list of products and their prices from the inputted string that matched a product in the products.csv file.
    Outputting an error print if any inputted product names didn't match any in products.csv. Made by KRYSTEN SCASE, 400628749'''
    file = open("products.csv") #open file
    wanted_products = products.split(" ") # List of products that were in the string of "products"
    final_list = []
    products_file = []

    for line in file: # Stripping white space from lines and appending to product_file list, making a 2D list of available products
        line_copy = line
        line_copy = line_copy.strip()
        products_file.append(line_copy.split(","))

    for index in range(len(products_file)): # Turning price values into integers or float if price isn't a whole number
        if "." in products_file[index][1]:
            products_file[index][1] = float(products_file[index][1])
        else:
            products_file[index][1] = int(products_file[index][1])

    for name in wanted_products:
        match = False
        for index in range(len(products_file)): # Checking for matches between list of available products and input string of wanted products
            if name == products_file[index][0]:
                match = True
                index_match = index
        if match == True: # Match
            final_list.append(products_file[index_match]) # Appending final list with matched product list and price
        elif match == False: # No Match (error)
            print(f"Error, product '{name}' not found")

    file.close()
    return final_list

#Line 146-300, helper function and pack_product proper starts
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
#Line 146-300, helper function and pack_product proper ends

def complete_order(userid, product_list):   #?Changes Required
    tax = 0.13   #sets tax to 0.13 percent
    random_discount = random.uniform(0.05,0.50)   #generates random float value between 0.05 and 0.50 for discount

    subtotal = 0   #sets subtotal to 0

    product = []   #empty list to store product names

    for i in range(len(product_list)):   #for loop that appends product names from products.csv to product list
        product_names = product_list[i][0]
        product.append(product_names)
    ordered_products = ", ".join(product)

    print(ordered_products)

    for i in range(len(product_list)):   #for loop that calculates order subtotal based on price of ordered products
        price = float(product_list[i][1])
        subtotal += price

    discount = subtotal * random_discount   #calculates discount based on subtotal and random discoun value

    pre_tax_total = subtotal - discount   #calculates pre-tax price of order

    tax_applied = pre_tax_total * tax   #calculates tax on order

    total = round(pre_tax_total + tax_applied, 2)   #calculates order total and rounds it to 2 decimal places

    total = str(total)

    order_count = 0   #initializes order count to keep track of customer orders

    filename = "orders.csv"   #sets filename to orders.csv so it can be opened later

    file = open(filename, "r")   #opens orders.csv to read from

    for line in file:   # for loop that runs through each line in the file to find other instances of orders by user
        for word in line.split(","):  
            if word == userid:
                order_count += 1

    file.close()

    file = open(filename, "a")   #opens orders.csv to append new order

    file.write(userid + ", " + total + ", " + ordered_products + "\n")   #writes user order and total under userid
    order_count += 1

    print(order_count)

    print("\n   FRI-12 Warehouse   ")   #print statements that print formatted reciept 
    print(f"-" * 25)

    for i in range(len(product_list)):
        product_name = product_list[i][0]
        product_price = float(product_list[i][1])
        print(f"{product_name:<11}{'$' + format(float(product_price), ',.2f'):>15}")

    print("-" * 25)
    print(f"{'Subtotal':<10}{'$' + format(subtotal, ',.2f'):>15}")
    print(f"{'Discount':<10}{'$' + format(discount, ',.2f'):>15}")
    print(f"{'Tax':<10}{'$' + format(tax_applied, ',.2f'):>15}")
    print(f"{'Total':<10}{'$' + format(float(total), ',.2f'):>15}")

def customer_summary(userid):   #?Changes Required
    file = open("products.csv",'r')
    products = []

    for line in file:
        name = line.strip().split(",")
        products.append(name[0])

    file.close()
   
    product_count = [0]*len(products)

    validation = False
    num_orders = 0
    total_spent = 0

    file = open("orders.csv",'r')
    for line in file:
        line = line.strip().split(",")

        if line[0] == userid:
            validation = True
            num_orders += 1
            total_spent += float(line[1])

            for i in range (len(products)):
                for i2 in range (2,len(line)):
                    if line[i2].strip() == products[i]:
                        product_count[i] += 1


    if validation is True:
        print("===================================")
        print(f" Customer Summary for {userid}")
        print("===================================")
        print(f" Total Orders : {num_orders}")
        print(f" Total Spent  : ${total_spent:.2f}")
        print("------------ Products -------------")

        for i in range(len(products)):
            if product_count[i] != 0: #print product quantity if not 0
                print(f"{products[i]:<15}| {product_count[i]}")
        print("===================================")

    else:
        print("Invalid username")

##*Code starts here
#Setting up the work directory to where ever the main.py is, useful for file paths
location=os.path.dirname(__file__)
os.chdir(location)
##Welcome the user
print('='*30)
print("Welcome to Fri-12 Warehouse")
print('='*30+'\n')

##Login the user  
user=authenticate()

while True:
    ##Scans items   
    # scanned_list=BarcodeScanner.scan_barcode()    #!UNCOMMENT BEFORE DEMO
    scanned_list="D12 Sponge WitchHat test" #!REMOVE BEFORE DEMO

    ##Looks up items and their prices
    product_list=lookup_products(scanned_list)
    print(f"product_list: {product_list}")

    ##Order the Q-arm to move the items
    # pack_products(product_list)    #!UNCOMMENT BEFORE DEMO

    ##Calculate total & record order in csv
    complete_order(user,product_list)

    ##Ask the user if they want to continue or quit
    if (not bool(input("Enter anything to make another order, enter nothing to see summary and quit.\n"))):
        break

##Summarize customer order history
customer_summary(user)