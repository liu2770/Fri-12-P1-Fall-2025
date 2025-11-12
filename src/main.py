"""
The main file for P1 Q-arm program.
Fri-12 P1, 2025 Fall
"""
from p1_functions.auth import authenticate  #Doing all of them in "from... import" form to cut the busy work
from p1_functions.signup import sign_up
from p1_functions.completeOrder import complete_order
from p1_functions.customerSummary import customer_summary
from p1_functions.lookUpProducts import lookup_products
from p1_functions.packProducts import pack_products
import os

#Setting up the work directory to where ever the main.py is, useful for file paths
location=os.path.dirname(__file__)
os.chdir(location)

##*Code starts here
#TODO: Implement a skeletal structure following the outlined sequence of events
##Login the user  
user=authenticate()

while True:
    ##Scans items   #?Eh no clue what to do here, I don't really see anywhere explicitly lay out the instruction for this.

    ##Looks up items and their prices
    product_list=lookup_products(scanned_list)

    ##Order to Q-arm to move the items
    # product_list = []
    # file = open("./content/products.csv", "r")
    # for line in file:
    #     product = []
    #     for word in line.split(","):
    #         product.append(word)
    #     product_list.append(product)
    pack_products(product_list) 

    ##Calculate total & record order in csv
    complete_order(user,product_list)

    ##Ask the user if they want to continue or quit
    if (not bool(input("Enter anything to make another order, enter nothing to see summary and quit.\n"))):
        break

##Summarize customer order history
customer_summary(user)