"""
The main file for P1 Q-arm program. This version combines
all files into one in case there is issues with loading the
normal file structure.
Fri-12 P1, 2025 Fall
"""
import csv
import bcrypt
import re

#Functions
def sign_up():
    # ask for user id and clean spaces
    userid = input("Enter a new user ID: ").strip()
    # read existing users
    with open("content/users.csv", "r", newline="") as f:
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
    with open("content/users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([userid, hashed_pw])

    print("Account created.")

def loadUserEntry():   
    """
    Helper function, handels read from users.csv. Return 
    a 2D list consists of user names and corresponding 
    passwords.
    """
    userList=[]
    with open("users.csv",newline='') as file:
        csvReader=csv.reader(file)
        # fileLines=file.read().split(sep="\n")
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
                input("Password does not match, enter anything to try again...")    #use input to pause the program so user can read the output
        else:
            input("User not found, enter anything to try again...")

def lookup_products(products):
    '''Returns a 2D list of products and their prices from the inputted string that matched a product in the products.csv file.
    Outputting an error print if any inputted product names didn't match any in products.csv'''
    file = open("products.csv") #open file
    wanted_products = products.split(",") # List of products that were in the string of "products"
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

def pack_products(product_list):
    for product in product_list:
        if product in product_list:
            ##Product moving code
            print(f"{product[0]} has been packed")
        else:
            print("The product you are looking for is not available, please try again")
    print("testing!")   #!Remove this line, stub
    return

def complete_order(userid, product_list):
    #TODO: put your code here
    print("testing!")   #!Remove this line, stub
    return

def customer_summary(userid):
    file = open("orders.csv",'r')
    validation = False
    userlines = []
    for line in file:
        line = line.strip().split(",")
        if line[0] == userid:
            validation = True
            userlines.append(line)

    if validation is True:
        num_orders = len(userlines)  # total number of orders
        total_spent = 0.0
        product_count = [0, 0, 0, 0, 0, 0]
        products = ["Sponge", "Bottle", "Rook", "D12", "Bowl", "WitchHat"]

        for order in userlines:
            product = str(order[1])
            qty = int(order[2])
            price = float(order[3])
            total_spent += qty * price  # total spent of orders

            for i in range(len(products)):  #store quantity of each product into the list
                if product == products[i]:
                    product_count[i] += qty

        print("===================================")
        print(f" Customer Summary for {userid}")
        print("===================================")
        print(f" Total Orders : {num_orders}")
        print(f" Total Spent  : ${total_spent:.2f}")
        print("------------ Products -------------")

        for i in range(len(products)):
            if product_count[i] != 0:   #print product quantity if not 0
                print(f"{products[i]}             | {product_count[i]}")
                
        print("===================================")

    else:
        print("Invalid username")

while True:
    ##Login the user  
    user=authenticate()
    if user==None:
        print("Order canceled")
        break

    ##Scans items   
    # load_barcodes()

    ##Looks up items and their prices
    # product_list=lookup_products(scanned_list)

    ##Order to Q-arm to move the items
    product_list = []
    file = open("products.csv", "r")
    for line in file:
        product = []
        for word in line.split(","):
            product.append(word)
        product_list.append(product)
    pack_products(product_list) 

    ##Calculate total & record order in csv
    complete_order(user,product_list)

    ##Ask the user if they want to continue or quit
    if (not bool(input("Enter anything to make another order, enter nothing to see summary and quit.\n"))):
        break

##Summarize customer order history
#customer_summary(input("Please enter the user ID to see its account summary: "))   #!Skipped for now 