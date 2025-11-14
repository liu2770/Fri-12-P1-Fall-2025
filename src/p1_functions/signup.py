import csv
import lib.bcrypt
import re

def sign_up():
    while True:
        userid = input("Enter a new user ID: ").strip()
        used = False

        with open("contents/users.csv", "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0 and row[0] == userid:
                    print("User ID already exists. Try another.")
                    used = True
                    break

        if not used:
            break

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!.@#$%^&*()_\[\]]).{6,}$'

    while True:
        password = input("Enter password (or type CANCEL): ").strip()
        if password.upper() == "CANCEL":
            print("Sign up cancelled.")
            return
        if re.match(pattern, password):
            break
        print("Password not strong enough. Try again.")

    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    with open("contents/users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([userid, hashed_pw])

    print("Account created.")
