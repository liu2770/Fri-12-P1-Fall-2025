import csv
import bcrypt
import re

def sign_up():
    # ask for user id
    userid = input("Enter a new user ID: ").strip()

    # read all existing ids (simple loop)
    existing_ids = []
    with open("contents/users.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            existing_ids.append(row[0])

    if userid in existing_ids:
        print("User ID already exists.")
        return

    # keep trying passwords until valid or cancelled
    while True:
        password = input("Enter password (or type CANCEL): ").strip()

        if password == "CANCEL":
            print("Sign-up cancelled.")
            return

        # regex for password rules
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!.@#$%^&*()_\[\]]).{6,}$'

        if re.match(pattern, password):
            break
        else:
            print("Password does not meet requirements. Try again.")

    # hash the password
    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # write the userid + hashed password
    with open("contents/users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([userid, hashed_pw])

    print("Account created.")
