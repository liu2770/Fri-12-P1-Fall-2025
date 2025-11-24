"""
The main file for P1 Q-arm program.
Fri-12 P1, 2025 Fall
"""
from p1_functions.auth import authenticate  #Doing all of them in "from... import" form to cut the busy work
from p1_functions.signup import sign_up
from p1_functions.completeOrder import complete_order
from p1_functions.customerSummary import customer_summary
from p1_functions.lookUpProducts import lookup_products
#from p1_functions.packProducts import pack_products    #!UNCOMMENT BEFORE DEMO
#from Common.qarm_interface_wrapper import *    #!UNCOMMENT BEFORE DEMO
import os

#Setting up the work directory to where ever the main.py is, useful for file paths
location=os.path.dirname(__file__)
os.chdir(location)

##*Code starts here
##Welcome the user
print('='*30)
print("Welcome to Fri-12 Warehouse")
print('='*30+'\n')

##Login the user  
user=authenticate()

while True:
    ##Scans items   
    #scanned_list=BarcodeScanner.scan_barcode()    #!UNCOMMENT BEFORE DEMO
    scanned_list="D12 Sponge WitchHat test"

    ##Looks up items and their prices
    product_list=lookup_products(scanned_list)
    print(f"product_list: {product_list}")

    ##Order the Q-arm to move the items
    #pack_products(product_list)    #!UNCOMMENT BEFORE DEMO

    ##Calculate total & record order in csv
    complete_order(user,product_list)

    ##Ask the user if they want to continue or quit
    if (not bool(input("Enter anything to make another order, enter nothing to see summary and quit.\n"))):
        break

##Summarize customer order history
customer_summary(user)