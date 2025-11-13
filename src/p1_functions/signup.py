import csv
import lib.bcrypt
import re
import os

def sign_up():
    userid = input("Enter a new user ID: ").strip()

    # if os.path.exists("users.csv"): #?We dont really need to verify the existance of the file here, also see readme for handling File IO
    with open("./content/users.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0 and row[0] == userid:
                print("User ID already exists. Please choose another one.")
                return

    password = input("Enter a password: ").strip()

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!.@#$%^&*()_\[\]]).{6,}$'
    if not re.match(pattern, password):
        print("Password must be at least 6 characters and contain one uppercase letter, one lowercase letter, one digit, and one symbol (!.@#$%^&*()_[])")
        return  #!Should not just boot the user out of the sign up process, instead let the user to try again

    hashed_pw = lib.bcrypt.hashpw(password.encode("utf-8"), lib.bcrypt.gensalt()).decode("utf-8")

    with open("./content/users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([userid, hashed_pw])

    print("Account created successfully!")
