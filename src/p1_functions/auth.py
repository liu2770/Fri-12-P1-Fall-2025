from p1_functions.signup import sign_up
import lib.bcrypt   #included in lib folder
import csv

def loadUserEntry(): 
    """
    Helper function, handels read from users.csv. Return 
    a 2D list consists of user names and corresponding 
    passwords.
    Jincheng Liu
    """
    userList=[]
    with open("./content/users.csv",newline='') as file:
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
            if lib.bcrypt.checkpw(password.encode('utf-8'),expectedPassword.encode('utf-8')):    #?Exit2
                print(f"User authentication acknowledged, welcome {userName}.")
                return userName
            else:
                input("Password does not match, enter anything to try again...")    #use input to pause the program so user can read the output
        else:
            input("User not found, enter anything to try again...")