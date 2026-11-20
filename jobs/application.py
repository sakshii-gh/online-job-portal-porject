

import json
import os
from jobs import load_jobs

# Create data folder
if not os.path.exists("data"):
    os.makedirs("data")

APPLICATION_FILE = "data/applications.json"


# Load application records
def load_applications():

    if os.path.exists(APPLICATION_FILE):
        with open(APPLICATION_FILE, "r") as file:
            return json.load(file)

    return []


# Save application records
def save_applications(applications):

    with open(APPLICATION_FILE, "w") as file:
        json.dump(applications, file, indent=4)


# Apply for a job
def apply_job():

    jobs = load_jobs()
    applications = load_applications()

    print("\n========== APPLY FOR JOB ==========")

    email = input("Enter your registered email: ")
    job_id = input("Enter Job ID: ")

    # Check whether job exists
    selected_job = None

    for job in jobs:
        if str(job["job_id"]) == job_id:
            selected_job = job
            break

    if selected_job is None:
        print("Job not found!")
        return

    # Check duplicate application
    for application in applications:

        if (application["email"] == email and
                application["job_id"] == int(job_id)):

            print("You have already applied for this job!")
            return

    # Generate application ID
    application_id = max(
        [app["application_id"] for app in applications],
        default=0
    ) + 1

    new_application = {
        "application_id": application_id,
        "email": email,
        "job_id": int(job_id),
        "job_title": selected_job["title"],
        "company": selected_job["company"],
        "status": "Pending"
    }

    applications.append(new_application)

    save_applications(applications)

    print("\nApplication Submitted Successfully!")
    print("Application ID:", application_id)
    print("Application Status: Pending")


# View all applications
def view_applications():

    applications = load_applications()

    print("\n========== ALL APPLICATIONS ==========")

    if not applications:
        print("No applications found.")
        return

    for application in applications:

        print("\nApplication ID:",
              application["application_id"])

        print("Candidate Email:",
              application["email"])

        print("Job Title:",
              application["job_title"])

        print("Company:",
              application["company"])

        print("Status:",
              application["status"])


# Update application status
def update_application_status():

    applications = load_applications()

    print("\n========== UPDATE APPLICATION STATUS ==========")

    application_id = input("Enter Application ID: ")

    for application in applications:

        if str(application["application_id"]) == application_id:

            print("\n1. Pending")
            print("2. Shortlisted")
            print("3. Rejected")

            choice = input("Select new status: ")

            if choice == "1":
                application["status"] = "Pending"

            elif choice == "2":
                application["status"] = "Shortlisted"

            elif choice == "3":
                application["status"] = "Rejected"

            else:
                print("Invalid choice!")
                return

            save_applications(applications)

            print("\nApplication Status Updated Successfully!")
            return

    print("Application not found!")


# Application management menu
def application_menu():

    while True:

        print("\n========== APPLICATION MANAGEMENT ==========")

        print("1. Apply for Job")
        print("2. View Applications")
        print("3. Update Application Status")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            apply_job()

        elif choice == "2":
            view_applications()

        elif choice == "3":
            update_application_status()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")
