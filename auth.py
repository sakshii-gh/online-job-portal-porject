

import json
import os
import hashlib

# Create data folder
if not os.path.exists("data"):
    os.makedirs("data")

# User data file
USER_FILE = "data/users.json"


# Read user records
def load_users():

    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)

    return []


# Save user records
def save_users(users):

    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


# Password encryption using hashing
def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


# Job seeker registration
def jobseeker_register():

    print("\n----- JOB SEEKER REGISTRATION -----")

    name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    users = load_users()

    for user in users:
        if user["email"] == email:
            print("Email already registered!")
            return

    new_user = {
        "name": name,
        "email": email,
        "password": hash_password(password),
        "role": "jobseeker"
    }

    users.append(new_user)
    save_users(users)

    print("\nJob Seeker Registration Successful!")


# Recruiter registration
def recruiter_register():

    print("\n----- RECRUITER REGISTRATION -----")

    name = input("Enter Recruiter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    users = load_users()

    for user in users:
        if user["email"] == email:
            print("Email already registered!")
            return

    new_user = {
        "name": name,
        "email": email,
        "password": hash_password(password),
        "role": "recruiter"
    }

    users.append(new_user)
    save_users(users)

    print("\nRecruiter Registration Successful!")


# Job seeker login
def jobseeker_login():

    print("\n----- JOB SEEKER LOGIN -----")

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    users = load_users()

    for user in users:
        if (user["email"] == email and
                user["password"] == hash_password(password) and
                user["role"] == "jobseeker"):

            print("\nLogin Successful!")
            print("Welcome", user["name"])
            return

    print("\nInvalid Email or Password!")


# Recruiter login
def recruiter_login():

    print("\n----- RECRUITER LOGIN -----")

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    users = load_users()

    for user in users:
        if (user["email"] == email and
                user["password"] == hash_password(password) and
                user["role"] == "recruiter"):

            print("\nLogin Successful!")
            print("Welcome", user["name"])
            return

    print("\nInvalid Email or Password!")
