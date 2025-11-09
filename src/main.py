"""
The main file for P1 Q-arm program.
Fri-12 P1, 2025 Fall
"""

##Imports
from p1_functions.auth import authenticate  #Doing all of them in "from... import" form to cut the busy work
from p1_functions.signup import sign_up
from p1_functions.completeOrder import complete_order
from p1_functions.customerSummary import customer_summary
from p1_functions.lookUpProducts import lookup_products
from p1_functions.packProducts import pack_products
import os

##*Code starts here

#Setting up the work directory to where ever the main.py is, useful for file paths
location=os.path.dirname(__file__)
os.chdir(location)

product_list = []

file = open("./content/products.csv", "r")

for line in file:
    product = []
    for word in line.split(","):
        product.append(word)
    product_list.append(product)
pack_products(product_list)
