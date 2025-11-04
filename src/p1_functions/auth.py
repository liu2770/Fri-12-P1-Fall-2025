from p1_functions.signup import sign_up
import bcrypt   #included in lib folder

def loadUserEntry():
    """
    Helper function, handels read from user.csv. Return 
    a 2D list consists of user names and corresponding 
    passwords.
    """
    file=open("./content/user.csv","r")
    userList=[]
    fileLines=file.read().split(sep="\n")
    for line in fileLines:
        userEntry=line.split(sep=', ')  #!Will broke if sign_up() doesn't follow the exact pattern
        userList.append(userEntry)
    file.close()
    return userList
    
def authenticate(): #TODO: Implement the ability to accept and recognize encrypted passwords
    """
    Handles the entire login authentication process.
    Asks the user to input their user name and password,
    if they dont have one call sign_up(). Return
    the user name upon successful authentication,
    let them keep trying if not. Reads from users.csv
    """
    ##Start of the program
    #Proceed to authenticate the user with a while loop
    while True:
        #Ask the user to input their user name, if they dont have one they should let the program know by putting "-1"
        userName=input("Please enter your user name now, enter -1 if you dont have one; quit() for quit: ")  #?Accepts any string at the moment

        #check if sign_up call is needed
        if userName=="quit()":  #?Exit 1
            return None #Incase user just want to quit
        if userName=="-1":
            sign_up()
            input("Sign up complete, enter anything to continue...")
        
        #Load the user entry, incase a new user has been added 
        userList=loadUserEntry()

        print(userList)#debug

        #Check if the user name exists
        userExist=False #Default states for userExist and userIndex
        uesrIndex=-1    
        for entry in userList:  #!When there are multiple same user names only the first would be recognized
            if entry[0]==userName:
                userExist=True
                uesrIndex=userList.index(entry)
                print(entry)
                print(uesrIndex)
                print(userList[uesrIndex])
        
        if userExist==True:
            password=input("User found, please input password now: ")
            if userList[uesrIndex][1]==password:    #?Exit2
                print(f"User authentication acknowledged, welcome {userName}.")
                return userName
            else:
                input("Password does not match, enter anything to try again...")    #use input to pause the program so user can read the output
        else:
            input("User not found, enter anything to try again...")