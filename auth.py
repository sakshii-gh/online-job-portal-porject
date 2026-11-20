import json
import os
import hashlib

DATA_FILE = "data/users.json"


# Create data folder if it does not exist
os.makedirs("data", exist_ok=True)


# Load users from JSON file
def load_users():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


# Save users to JSON file
def save_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)


# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Job Seeker Registration
def jobseeker_register():

    print("\n--- Job Seeker Registration ---")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter password: ")

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

    print("Job Seeker registered successfully!")


# Recruiter Registration
def recruiter_register():

    print("\n--- Recruiter Registration ---")

    name = input("Enter recruiter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

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

    print("Recruiter registered successfully!")


# Job Seeker Login
def jobseeker_login():

    print("\n--- Job Seeker Login ---")

    email = input("Enter email: ")
    password = input("Enter password: ")

    users = load_users()

    for user in users:
        if (user["email"] == email
                and user["password"] == hash_password(password)
                and user["role"] == "jobseeker"):

            print("Login successful!")
            return user

    print("Invalid email or password!")
    return None


# Recruiter Login
def recruiter_login():

    print("\n--- Recruiter Login ---")

    email = input("Enter email: ")
    password = input("Enter password: ")

    users = load_users()

    for user in users:
        if (user["email"] == email
                and user["password"] == hash_password(password)
                and user["role"] == "recruiter"):

            print("Login successful!")
            return user

    print("Invalid email or password!")
    return None
