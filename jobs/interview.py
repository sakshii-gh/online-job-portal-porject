

import json
import os
from applications import load_applications

# Create data folder
if not os.path.exists("data"):
    os.makedirs("data")

INTERVIEW_FILE = "data/interviews.json"


# Load interview records
def load_interviews():

    if os.path.exists(INTERVIEW_FILE):
        with open(INTERVIEW_FILE, "r") as file:
            return json.load(file)

    return []


# Save interview records
def save_interviews(interviews):

    with open(INTERVIEW_FILE, "w") as file:
        json.dump(interviews, file, indent=4)


# Schedule an interview
def schedule_interview():

    applications = load_applications()
    interviews = load_interviews()

    print("\n========== SCHEDULE INTERVIEW ==========")

    application_id = input("Enter Application ID: ")

    selected_application = None

    # Check application
    for application in applications:

        if str(application["application_id"]) == application_id:
            selected_application = application
            break

    if selected_application is None:
        print("Application not found!")
        return

    # Check application status
    if selected_application["status"] != "Shortlisted":
        print("Interview can only be scheduled for shortlisted candidates!")
        return

    # Check duplicate interview
    for interview in interviews:

        if interview["application_id"] == int(application_id):
            print("Interview is already scheduled!")
            return

    interview_id = max(
        [item["interview_id"] for item in interviews],
        default=0
    ) + 1

    interview_date = input("Enter Interview Date (DD-MM-YYYY): ")
    interview_time = input("Enter Interview Time: ")
    interview_mode = input("Enter Interview Mode (Online/Offline): ")

    new_interview = {
        "interview_id": interview_id,
        "application_id": int(application_id),
        "candidate_email": selected_application["email"],
        "job_title": selected_application["job_title"],
        "company": selected_application["company"],
        "date": interview_date,
        "time": interview_time,
        "mode": interview_mode
    }

    interviews.append(new_interview)

    save_interviews(interviews)

    print("\nInterview Scheduled Successfully!")
    print("Interview ID:", interview_id)


# View scheduled interviews
def view_interviews():

    interviews = load_interviews()

    print("\n========== INTERVIEW SCHEDULE ==========")

    if not interviews:
        print("No interviews scheduled.")
        return

    for interview in interviews:

        print("\nInterview ID:", interview["interview_id"])
        print("Application ID:", interview["application_id"])
        print("Candidate Email:", interview["candidate_email"])
        print("Job Title:", interview["job_title"])
        print("Company:", interview["company"])
        print("Interview Date:", interview["date"])
        print("Interview Time:", interview["time"])
        print("Interview Mode:", interview["mode"])


# Interview management menu
def interview_menu():

    while True:

        print("\n========== INTERVIEW MANAGEMENT ==========")

        print("1. Schedule Interview")
        print("2. View Interviews")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            schedule_interview()

        elif choice == "2":
            view_interviews()

        elif choice == "3":
            break

        else:
            print("Invalid choice! Please try again.")
