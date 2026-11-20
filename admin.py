
from auth import load_users
from jobs import load_jobs
from applications import load_applications
from interviews import load_interviews


# Admin login
def admin_login():

    print("\n========== ADMIN LOGIN ==========")

    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    if username == "admin" and password == "admin123":

        print("\nAdmin Login Successful!")
        print("Welcome to Admin Dashboard")

        admin_dashboard()

    else:
        print("\nInvalid Admin Username or Password!")


# Admin dashboard
def admin_dashboard():

    while True:

        print("\n========== ADMIN DASHBOARD ==========")

        print("1. View Dashboard Statistics")
        print("2. View Registered Users")
        print("3. View Posted Jobs")
        print("4. View Job Applications")
        print("5. View Scheduled Interviews")
        print("6. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            dashboard_statistics()

        elif choice == "2":
            view_users()

        elif choice == "3":
            view_admin_jobs()

        elif choice == "4":
            view_admin_applications()

        elif choice == "5":
            view_admin_interviews()

        elif choice == "6":
            print("\nAdmin Logged Out Successfully!")
            break

        else:
            print("Invalid choice! Please try again.")


# Display dashboard statistics
def dashboard_statistics():

    users = load_users()
    jobs = load_jobs()
    applications = load_applications()
    interviews = load_interviews()

    jobseekers = 0
    recruiters = 0

    for user in users:

        if user["role"] == "jobseeker":
            jobseekers += 1

        elif user["role"] == "recruiter":
            recruiters += 1

    print("\n========== DASHBOARD STATISTICS ==========")

    print("Total Job Seekers:", jobseekers)
    print("Total Recruiters:", recruiters)
    print("Total Jobs:", len(jobs))
    print("Total Applications:", len(applications))
    print("Total Interviews:", len(interviews))


# View registered users
def view_users():

    users = load_users()

    print("\n========== REGISTERED USERS ==========")

    if not users:
        print("No users registered.")
        return

    for user in users:

        print("\nName:", user["name"])
        print("Email:", user["email"])
        print("Role:", user["role"])


# View posted jobs
def view_admin_jobs():

    jobs = load_jobs()

    print("\n========== POSTED JOBS ==========")

    if not jobs:
        print("No jobs available.")
        return

    for job in jobs:

        print("\nJob ID:", job["job_id"])
        print("Job Title:", job["title"])
        print("Company:", job["company"])
        print("Location:", job["location"])


# View job applications
def view_admin_applications():

    applications = load_applications()

    print("\n========== JOB APPLICATIONS ==========")

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

        print("Status:",
              application["status"])


# View scheduled interviews
def view_admin_interviews():

    interviews = load_interviews()

    print("\n========== SCHEDULED INTERVIEWS ==========")

    if not interviews:
        print("No interviews scheduled.")
        return

    for interview in interviews:

        print("\nInterview ID:", interview["interview_id"])
        print("Candidate:", interview["candidate_email"])
        print("Job Title:", interview["job_title"])
        print("Interview Date:", interview["date"])
        print("Interview Time:", interview["time"])
