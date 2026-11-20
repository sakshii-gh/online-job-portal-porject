
import os
import json
import shutil

# Create folders
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("resumes"):
    os.makedirs("resumes")

RESUME_FILE = "data/resumes.json"


# Load resume records
def load_resumes():

    if os.path.exists(RESUME_FILE):
        with open(RESUME_FILE, "r") as file:
            return json.load(file)

    return []


# Save resume records
def save_resumes(resumes):

    with open(RESUME_FILE, "w") as file:
        json.dump(resumes, file, indent=4)


# Upload candidate resume
def upload_resume():

    resumes = load_resumes()

    print("\n========== UPLOAD RESUME ==========")

    email = input("Enter your registered email: ")

    file_path = input("Enter the complete path of your resume: ")

    # Check whether file exists
    if not os.path.isfile(file_path):
        print("Resume file not found!")
        return

    # Check file extension
    extension = os.path.splitext(file_path)[1].lower()

    if extension not in [".pdf", ".doc", ".docx"]:
        print("Only PDF, DOC and DOCX files are allowed!")
        return

    # Generate resume ID
    resume_id = max(
        [resume["resume_id"] for resume in resumes],
        default=0
    ) + 1

    file_name = "resume_" + str(resume_id) + extension

    destination = os.path.join("resumes", file_name)

    # Copy resume into project folder
    shutil.copy2(file_path, destination)

    new_resume = {
        "resume_id": resume_id,
        "email": email,
        "file_name": file_name,
        "file_path": destination
    }

    resumes.append(new_resume)

    save_resumes(resumes)

    print("\nResume Uploaded Successfully!")
    print("Resume ID:", resume_id)


# View uploaded resumes
def view_resumes():

    resumes = load_resumes()

    print("\n========== UPLOADED RESUMES ==========")

    if not resumes:
        print("No resumes uploaded.")
        return

    for resume in resumes:

        print("\nResume ID:", resume["resume_id"])
        print("Candidate Email:", resume["email"])
        print("File Name:", resume["file_name"])
        print("File Path:", resume["file_path"])


# Resume management menu
def resume_menu():

    while True:

        print("\n========== RESUME MANAGEMENT ==========")

        print("1. Upload Resume")
        print("2. View Resumes")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            upload_resume()

        elif choice == "2":
            view_resumes()

        elif choice == "3":
            break

        else:
            print("Invalid choice!")
