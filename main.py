import auth
import jobs
import applications
import interviews
import resume
import admin
import reports


# Job Seeker Dashboard
def jobseeker_dashboard(user):

    while True:
        print("\n===== JOB SEEKER DASHBOARD =====")
        print("Welcome,", user["name"])

        print("\n1. View Jobs")
        print("2. Search Jobs")
        print("3. Job Details")
        print("4. Apply for Job")
        print("5. Upload Resume")
        print("6. View Interviews")
        print("7. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            jobs.view_jobs()

        elif choice == "2":
            jobs.search_jobs()

        elif choice == "3":
            jobs.job_details()

        elif choice == "4":
            applications.apply_job()

        elif choice == "5":
            resume.upload_resume()

        elif choice == "6":
            interviews.view_interviews()

        elif choice == "7":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice! Try again.")


# Recruiter Dashboard
def recruiter_dashboard(user):

    while True:
        print("\n===== RECRUITER DASHBOARD =====")
        print("Welcome,", user["name"])

        print("\n1. Add Job")
        print("2. View Jobs")
        print("3. Edit Job")
        print("4. Delete Job")
        print("5. View Applications")
        print("6. Update Application Status")
        print("7. Schedule Interview")
        print("8. View Interviews")
        print("9. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            jobs.add_job()

        elif choice == "2":
            jobs.view_jobs()

        elif choice == "3":
            jobs.edit_job()

        elif choice == "4":
            jobs.delete_job()

        elif choice == "5":
            applications.view_applications()

        elif choice == "6":
            applications.update_application_status()

        elif choice == "7":
            interviews.schedule_interview()

        elif choice == "8":
            interviews.view_interviews()

        elif choice == "9":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice! Try again.")


# Main Menu
def main():

    while True:

        print("\n================================")
        print("       ONLINE JOB PORTAL")
        print("================================")

        print("1. Job Seeker")
        print("2. Recruiter")
        print("3. Admin")
        print("4. Reports")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\n1. Register")
            print("2. Login")

            option = input("Enter your choice: ")

            if option == "1":
                auth.jobseeker_register()

            elif option == "2":
                user = auth.jobseeker_login()

                if user:
                    jobseeker_dashboard(user)

            else:
                print("Invalid choice!")

        elif choice == "2":

            print("\n1. Register")
            print("2. Login")

            option = input("Enter your choice: ")

            if option == "1":
                auth.recruiter_register()

            elif option == "2":
                user = auth.recruiter_login()

                if user:
                    recruiter_dashboard(user)

            else:
                print("Invalid choice!")

        elif choice == "3":
            if admin.admin_login():
                admin.admin_dashboard()

        elif choice == "4":
            reports.report_menu()

        elif choice == "5":
            print("Thank you for using Online Job Portal!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the project
if __name__ == "__main__":
    main()
