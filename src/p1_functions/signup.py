import csv
import lib.bcrypt
import re

def sign_up():
    # ask for user id and clean spaces
    userid = input("Enter a new user ID: ").strip()
    # read existing users
    with open("contents/users.csv", "r", newline="") as f:
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
    hashed_pw = lib.bcrypt.hashpw(password.encode("utf-8"), lib.bcrypt.gensalt()).decode("utf-8")
    with open("contents/users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([userid, hashed_pw])

    print("Account created.")
