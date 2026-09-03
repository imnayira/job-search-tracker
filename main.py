import csv
import os

def menu():
    print("""================================
JOB SEARCH TRACKER
================================

1. Add a job
2. View jobs
3. Search jobs
4. View "Applied" jobs
5. View jobs based on company name
6. Edit Status
7. Delete
8. Exit
\n
""")
    
def add_job(job_title, date, company_name, job_url, status, file_path):
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, job_title, company_name, job_url, status])
    print("Job added successfully!\n")

def delete_job(job_title, file_path):
    job_to_delete = search_by_job_title(job_title, file_path)
    if job_to_delete:
        with open(file_path, "r") as file:
            rows_to_keep = []
            reader = csv.DictReader(file)
            for row in reader:
                if row["Job Title"].lower() != job_to_delete["Job Title"].lower():
                    rows_to_keep.append(row)

        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames = ["Date", "Job Title", "Company", "Job URL", "Status"])
            writer.writeheader()
            writer.writerows(rows_to_keep)
        print("Deleted successfully!")




def view_jobs(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Date: {row['Date']}\nJob Title: {row['Job Title']}\nCompany: {row['Company']}\nJob URL: {row['Job URL']}\nStatus: {row['Status']}\n")

def search_by_job_title(job_title, file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if  job_title.lower() in row['Job Title'].lower():
                return row
        else:
            print("Job not found!")

def view_applied_jobs(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Status"].lower() == "applied":
                print(f"Date: {row['Date']}\nJob Title: {row['Job Title']}\nCompany: {row['Company']}\nJob URL: {row['Job URL']}\nStatus: {row['Status']}\n")

def view_jobs_by_company(company_name, file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if company_name.lower() == row["Company"].lower():
                print(f"Date: {row['Date']}\nJob Title: {row['Job Title']}\nCompany: {row['Company']}\nJob URL: {row['Job URL']}\nStatus: {row['Status']}\n")

def update_status(job_title,new_status,file_path):
    chosen_job = search_by_job_title(job_title, file_path)
    new_row = []
    if chosen_job:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Job Title"].lower() == chosen_job["Job Title"].lower():
                    row["Status"] = new_status
                new_row.append(row)
               
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames = ["Date", "Job Title", "Company", "Job URL", "Status"])
            writer.writeheader()
            writer.writerows(new_row)
   

file_path = "jobs_to_track.csv"
if not os.path.exists(file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Job Title", "Company", "Job URL", "Status"])
    


while True:
    menu()
    choice = input("Enter your choice from the menu above: \n").strip()
    if choice == "1":
        job_title = input("Enter job title: ").strip()
        if not job_title:
            print("Job title cannot be empty, try again!")
            continue
        company_name = input("Enter company: ").strip()
        date = input("Enter date: ")
        job_url = input("Enter URL: ")
        status = input("Enter status: ").strip()
        add_job(job_title, date, company_name, job_url, status, file_path)

    elif choice == "2":
        view_jobs(file_path)

    elif choice == "3":
        job_title_search = input("Enter the job title or a keyword in it: ").strip()
        print("\n")
        row = search_by_job_title(job_title_search, file_path)
        if row:
            print("Job found, details below: ")
            print(f"Date: {row['Date']}\nJob title: {row['Job Title']}\nCompany name: {row['Company']}\nJob URL: {row['Job URL']}\nStatus: {row['Status']}")

    elif choice == "4":
        view_applied_jobs(file_path)

    elif choice == "5":
        company_name_check = input("Enter the company name: ")
        view_jobs_by_company(company_name_check, file_path)

    elif choice == "6":
        job_to_update = input("Enter the name of the job you want to update: ")
        status_choice = input("Enter the new status (1- Saved, 2- Applied, 3- Interview, 4- Offer, 5- Rejected, 6- Withdrawn)\n")
        if status_choice == "1":
            new_status = "Saved"
            update_status(job_to_update, new_status, file_path)

        elif status_choice == "2":
            new_status = "Applied"
            update_status(job_to_update, new_status, file_path)

        elif status_choice == "3":
            new_status = "Interview"
            update_status(job_to_update, new_status, file_path)

        elif status_choice == "4":
            new_status = "Offer"
            update_status(job_to_update, new_status, file_path)

        elif status_choice == "5":
            new_status = "Rejected"
            update_status(job_to_update, new_status, file_path)

        elif status_choice == "6":
            new_status = "Withdrawn"
            update_status(job_to_update, new_status, file_path)

        else:
            print("Invalid choice")

        

    elif choice == "7":
        to_delete = input("Enter the title of the job you wanna delete: ")
        delete_job(to_delete, file_path)

    elif choice == "8":
        print("Ending program!")
        break

    else:
        print("Error, choice not found, kindly try again!")
   