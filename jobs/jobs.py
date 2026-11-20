
import json
import os

# Create data folder
if not os.path.exists("data"):
    os.makedirs("data")

JOB_FILE = "data/jobs.json"


# Load job records
def load_jobs():

    if os.path.exists(JOB_FILE):
        with open(JOB_FILE, "r") as file:
            return json.load(file)

    return []


# Save job records
def save_jobs(jobs):

    with open(JOB_FILE, "w") as file:
        json.dump(jobs, file, indent=4)


# Display all available jobs
def view_jobs():

    jobs = load_jobs()

    print("\n========== AVAILABLE JOBS ==========")

    if not jobs:
        print("No jobs available.")
        return

    for job in jobs:
        print("\nJob ID:", job["job_id"])
        print("Job Title:", job["title"])
        print("Company:", job["company"])
        print("Location:", job["location"])
        print("Salary:", job["salary"])


# Search jobs by title or location
def search_jobs():

    jobs = load_jobs()

    keyword = input("\nEnter job title or location: ").lower()

    found = False

    for job in jobs:

        if (keyword in job["title"].lower() or
                keyword in job["location"].lower()):

            print("\nJob ID:", job["job_id"])
            print("Title:", job["title"])
            print("Company:", job["company"])
            print("Location:", job["location"])
            print("Salary:", job["salary"])

            found = True

    if not found:
        print("No matching jobs found.")


# Display details of a selected job
def job_details():

    jobs = load_jobs()

    job_id = input("\nEnter Job ID: ")

    for job in jobs:

        if str(job["job_id"]) == job_id:

            print("\n========== JOB DETAILS ==========")
            print("Job ID:", job["job_id"])
            print("Title:", job["title"])
            print("Company:", job["company"])
            print("Location:", job["location"])
            print("Salary:", job["salary"])
            print("Description:", job["description"])
            print("Experience:", job["experience"])

            return

    print("Job not found!")


# Add a new job vacancy
def add_job():

    jobs = load_jobs()

    print("\n========== POST A NEW JOB ==========")

    job_id = max(
        [job["job_id"] for job in jobs],
        default=0
    ) + 1

    title = input("Enter Job Title: ")
    company = input("Enter Company Name: ")
    location = input("Enter Job Location: ")
    salary = input("Enter Salary: ")
    description = input("Enter Job Description: ")
    experience = input("Enter Required Experience: ")

    new_job = {
        "job_id": job_id,
        "title": title,
        "company": company,
        "location": location,
        "salary": salary,
        "description": description,
        "experience": experience
    }

    jobs.append(new_job)

    save_jobs(jobs)

    print("\nJob Posted Successfully!")
    print("Your Job ID is:", job_id)


# Edit an existing job
def edit_job():

    jobs = load_jobs()

    job_id = input("\nEnter Job ID to edit: ")

    for job in jobs:

        if str(job["job_id"]) == job_id:

            print("\nEnter Updated Job Details")

            job["title"] = input("Enter New Job Title: ")
            job["company"] = input("Enter New Company: ")
            job["location"] = input("Enter New Location: ")
            job["salary"] = input("Enter New Salary: ")
            job["description"] = input("Enter New Description: ")
            job["experience"] = input("Enter New Experience: ")

            save_jobs(jobs)

            print("\nJob Updated Successfully!")
            return

    print("Job not found!")


# Delete an existing job
def delete_job():

    jobs = load_jobs()

    job_id = input("\nEnter Job ID to delete: ")

    for job in jobs:

        if str(job["job_id"]) == job_id:

            jobs.remove(job)

            save_jobs(jobs)

            print("\nJob Deleted Successfully!")
            return

    print("Job not found!")


# Job management menu
def job_menu():

    while True:

        print("\n========== JOB MANAGEMENT ==========")
        print("1. View Jobs")
        print("2. Search Jobs")
        print("3. View Job Details")
        print("4. Add Job")
        print("5. Edit Job")
        print("6. Delete Job")
        print("7. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_jobs()

        elif choice == "2":
            search_jobs()

        elif choice == "3":
            job_details()

        elif choice == "4":
            add_job()

        elif choice == "5":
            edit_job()

        elif choice == "6":
            delete_job()

        elif choice == "7":
            break

        else:
            print("Invalid choice! Please try again.")
