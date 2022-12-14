import hashlib
from typing import List

def signup():
    status = input("Hi, are you a (f)reelancer or a (c)orporation?" + "\n")
    if status == "f":
        username = input("Enter freelancer username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        while 1:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open("freelancer_credentials.txt", "w") as f:
                    f.write(username + "\n")
                    f.write(hash1)
                f.close()
                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again. \n")
    elif status == "c":
        username = input("Enter corporation username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        while 1:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open("corp_credentials.txt", "w") as f:
                    f.write(username + "\n")
                    f.write(hash1)
                f.close()
                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again.\n")

def login():
    play = 4
    status = input("Are you a (f)reelancer or a (c)orporation?" + "\n")
    if status == "f":
        while play>=0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open("freelancer_credentials.txt", "r") as f:
                stored_fren_username, stored_password = f.read().split("\n")
            f.close()
            if username == stored_fren_username and auth_hash == stored_password:
                print("Logged in Successfully!")
                freelancer_page()
                break
            else:
                print("Login failed!, you have " , play , " attempts to try again\n")
                play=play-1
        if(play<0):
            print("you can't login, try creating account")
            signup()

    elif status == "c":
        while play >=0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open("corp_credentials.txt", "r") as f:
                stored_corp_username, stored_corp_password = f.read().split("\n")
            f.close()
            if username == stored_corp_username and auth_hash == stored_corp_password:
                print("Logged in Successfully!")
                corp_page()
                break
            else:
                print("Login failed!, you have ",play," attempts to try again\n")
                play=play-1
            if play <0:
                print("you can't login, try creating account")
                signup()

def corp_page():
    with open("corp_credentials.txt", "r") as f:
        stored_username, stored_password= f.read().split("\n")
        f.close()
        username = stored_username
        corp_chosen = input("Hi " + username + " Do you want to (l)ist a job or (v)iew applicants?")
        if corp_chosen == "l":
            xo = int(input("enter how many jobs you want to declare: "))
            lp = 1
            job = []
            xp = 0
            job_details = []
            while xo >= lp:
                print("job", lp)
                job.append(str(input("enter job title: ")))
                job_details.append(input("enter job description: "))
                if xp == 0:
                    with open("jobs.txt", "w") as f:
                        f.write(job[xp] + ":" + "\n")
                        f.write(job_details[xp] + "\n")
                else:
                    with open("jobs.txt", "a") as f:
                        f.write(job[xp] + ":" + "\n")
                        f.write(job_details[xp] + "\n")
                f.close()
                lp = lp + 1
                xp = xp + 1
        elif corp_chosen == "v":
            with open("job_applied.txt", "r")as f:
                job_applied = f.read()
                f.close()
            with open("applicant_description.txt", "r")as f:
                applicant_description = f.read()
                f.close()
            with open("freelancer_credentials.txt", "r") as f:
                stored_username = f.read().split("\n")
                f.close()
            print(stored_username[0] + " has applied to " + job_applied)

            print(stored_username[0] + "'s bio is: " + "\n" +applicant_description + "\n")
            job_status_1 = input("Wanna accept this application? (y/n): ")
            if job_status_1 == "y":
                job_status = "Accepted"
                with open("job_status.txt", "w") as f:
                    f.write(job_status)
                    f.close()

            else:
                job_status = "Not Accepted"
                with open("job_status.txt", "w") as f:
                    f.write(job_status)
                    f.close()



def freelancer_page():
    zero = 0
    global stored_fren_username
    with open("freelancer_credentials.txt", "r") as f:
        stored_fren_username, stored_password = f.read().split("\n")
        f.close()
        username = stored_fren_username
        print("Hi " + stored_fren_username + " there are some jobs available. Do you want to see them?\n")
        viewjobs = input("(y)es, or (n)o\n")
        if viewjobs == "y":
            with open("jobs.txt", "r") as f:
                job1 = f.read().split("\n")
                job1_details = f.read().split("\n")
                job2 = f.read().split("\n")
                job2_details = f.read().split("\n")
                job3 = f.read().split("\n")
                job3_details = f.read().split("\n")
                job4 = f.read().split("\n")
                job4_details = f.read().split("\n")
                job5 = f.read().split("\n")
                job5_details = f.read().split("\n")
                f.close()
            print("1-" + job1[0] + " \n" + job1[1] + "\n" + "2-" + job1[2] + "\n" + job1[3] + "\n" + "3-" + job1[4] + "\n" + job1[5] + "\n" + "4-" + job1[6] + "\n" + job1[7] + "\n" + "5-" + job1[8] + "\n" + job1[9] + "\n")
        pass
        job_apply = input("Do you want to apply for a (j)ob? or do you want to see job (s)tatus?" + "\n")
        while job_apply == "j":
            applicant_description = input("Please inter your bio: " + "\n")
            with open("applicant_description.txt", "w")as f:
                f.write(applicant_description + "\n")
                f.close()
            i = int(input("Please enter job's number " + "\n"))
            if i == 1:
                with open("job_applied.txt", "w") as f:
                    f.write(job1[0])
                    f.close()
            elif i == 2:
                with open("job_applied.txt", "w") as f:
                    f.write(job1[2])
                    f.close()
            elif i == 3:
                with open("job_applied.txt", "w") as f:
                    f.write(job1[4])
                    f.close()
            elif i == 4:
                with open("job_applied.txt", "w") as f:
                    f.write(job1[6])
                    f.close()
            elif i == 5:
                with open("job_applied.txt", "w") as f:
                    f.write(job1[8])
                    f.close()
            print("Job request sent successfully !")
            break
        with open("job_status.txt", "r")as f:
            job_status = f.read()
            f.close()
        while job_apply == "s":
            print("you " + "have been " + job_status + " to your job!" + "\n")
            break



while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
