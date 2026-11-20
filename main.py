

print("======================================")
print("          ONLINE JOB PORTAL")
print("======================================")

while True:

    print("\n------------- MAIN MENU -------------")
    print("1. Job Seeker")
    print("2. Recruiter")
    print("3. Admin")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n----- JOB SEEKER -----")
        print("1. Register")
        print("2. Login")

        option = input("Enter your choice: ")

        if option == "1":
            from auth import jobseeker_register
            jobseeker_register()

        elif option == "2":
            from auth import jobseeker_login
            jobseeker_login()

        else:
            print("Invalid choice!")

    elif choice == "2":
        print("\n----- RECRUITER -----")
        print("1. Register")
        print("2. Login")

        option = input("Enter your choice: ")

        if option == "1":
            from auth import recruiter_register
            recruiter_register()

        elif option == "2":
            from auth import recruiter_login
            recruiter_login()

        else:
            print("Invalid choice!")

    elif choice == "3":
        from admin import admin_login
        admin_login()

    elif choice == "4":
        print("\nThank you for using Online Job Portal!")
        break

    else:
        print("\nInvalid choice! Please try again.")
