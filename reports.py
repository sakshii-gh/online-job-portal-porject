

from auth import load_users
from jobs import load_jobs
from applications import load_applications
from interviews import load_interviews


# Generate user report
def user_report():

    users = load_users()

    jobseekers = 0
    recruiters = 0

    for user in users:

        if user["role"] == "jobseeker":
            jobseekers += 1

        elif user["role"] == "recruiter":
            recruiters += 1

    print("\n========== USER REPORT ==========")
    print("Total Registered Users:", len(users))
    print("Total Job Seekers:", jobseekers)
    print("Total Recruiters:", recruiters)


# Generate job report
def job_report():

    jobs = load_jobs()

    print("\n========== JOB REPORT ==========")
    print("Total Jobs Posted:", len(jobs))

    if not jobs:
        print("No jobs available.")
        return

    for job in jobs:

        print("\nJob ID:", job["job_id"])
        print("Job Title:", job["title"])
        print("Company:", job["company"])
        print("Location:", job["location"])


# Generate application report
def application_report():

    applications = load_applications()

    pending = 0
    shortlisted = 0
    rejected = 0

    for application in applications:

        if application["status"] == "Pending":
            pending += 1

        elif application["status"] == "Shortlisted":
            shortlisted += 1

        elif application["status"] == "Rejected":
            rejected += 1

    print("\n========== APPLICATION REPORT ==========")
    print("Total Applications:", len(applications))
    print("Pending Applications:", pending)
    print("Shortlisted Applications:", shortlisted)
    print("Rejected Applications:", rejected)


# Generate interview report
def interview_report():

    interviews = load_interviews()

    print("\n========== INTERVIEW REPORT ==========")
    print("Total Interviews Scheduled:", len(interviews))

    for interview in interviews:

        print("\nCandidate:", interview["candidate_email"])
        print("Job:", interview["job_title"])
        print("Date:", interview["date"])
        print("Time:", interview["time"])


# Reports menu
def report_menu():

    while True:

        print("\n========== REPORTS MENU ==========")

        print("1. User Report")
        print("2. Job Report")
        print("3. Application Report")
        print("4. Interview Report")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            user_report()

        elif choice == "2":
            job_report()

        elif choice == "3":
            application_report()

        elif choice == "4":
            interview_report()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")
