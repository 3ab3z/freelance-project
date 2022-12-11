import hashlib                                                                 #عشان اشفر الباسورد
a = ""
b = ""
job_status = ""



def signup():                                                                  #دي الدالة اللي هيبقى تحتها الأوامر بتاعة التسجيل لأول مرة
    status = input("Hi, are you a (f)reelancer or a (c)orporation?" + "\n")    #هنا بقوله انت فريلانسر ولا شركة؟
    if status == "f":
        username = input("Enter freelancer username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        if conf_pwd == password:  # هنا بقول لو الباسورد اتكتب مرتين صح شفرهولي، لو متكتبش صح قول إن في حاجة غلط
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("freelancer_credentials.txt", "w") as f:  # هنا انا بخزن اسم المستخدم و الباسورد و حالة المستخدم في فايل خارجي
                f.write(username + "\n")
                f.write(hash1)
            f.close()
            print("You have registered successfully!")
        else:
            print("Password is not same as above! \n")
    elif status == "c":
        username = input("Enter corporation username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        if conf_pwd == password:  # هنا بقول لو الباسورد اتكتب مرتين صح شفرهولي، لو متكتبش صح قول إن في حاجة غلط
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("corp_credentials.txt", "w") as f:  # هنا انا بخزن اسم المستخدم و الباسورد و حالة المستخدم في فايل خارجي
                f.write(username + "\n")
                f.write(hash1)
            f.close()
            print("You have registered successfully!")
        else:
            print("Password is not same as above! \n")

def login():                                                                   #دي الدالة بتاعة تسجيل الدخول لمستخدم موجود
    status = input("Are you a (f)reelancer or a (c)orporation?" + "\n")
    if status == "f":
        username = input("Enter username: ")
        password = input("Enter password: ")
        auth = password.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open("freelancer_credentials.txt", "r") as f:  # هنا انا هقرأ البيانات اللي موجودة في الفايل الخارجي
            stored_fren_username, stored_password = f.read().split("\n")
        f.close()
        if username == stored_fren_username and auth_hash == stored_password:
            print("Logged in Successfully!")
            freelancer_page()
        else:
            print("Login failed! \n")
    elif status == "c":
        username = input("Enter username: ")
        password = input("Enter password: ")
        auth = password.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open("corp_credentials.txt", "r") as f:  # هنا انا هقرأ البيانات اللي موجودة في الفايل الخارجي
            stored_corp_username, stored_corp_password = f.read().split("\n")
        f.close()
        if username == stored_corp_username and auth_hash == stored_corp_password:
            print("Logged in Successfully!")
            corp_page()
        else:
            print("Login failed! \n")

def corp_page():                                                               #هنا أنا بعرف الدالة اللي هيبقى تحتها صفحة الشركة
    with open("corp_credentials.txt", "r") as f:
        stored_username, stored_password= f.read().split("\n")
        f.close()
        username = stored_username
        corp_chosen = input("Hi " + username + " Do you want to (l)ist a job or (v)iew applicants?")
        job1 = ""
        job2 = ""
        job3 = ""
        job4 = ""
        job5 = ""
        status = ""
        if corp_chosen == "l":
            job1 = input("Please enter the job1's name: " + "\n")
            job2 = input("Please enter the job2's name: " + "\n")
            job3 = input("Please enter the job3's name: " + "\n")
            job4 = input("Please enter the job4's name: " + "\n")
            job5 = input("Please enter the job5's name: " + "\n")
            with open("jobs.txt", "w") as f:
                f.write(job1 + "\n")
                f.write(job2 + "\n")
                f.write(job3 + "\n")
                f.write(job4 + "\n")
                f.write(job5)
            f.close()
        elif corp_chosen == "v":
            with open("freelancer_credentials.txt", "r") as f:
                stored_username = f.read().split("\n")
                f.close()
            print("freelancer")
            print(" Has applied to a job")
            job_status_1 = input("Wanna accept this application? (y/n): ")
            if job_status_1 == "y":
                job_status = "Accepted"
            else:
                job_status = "Not Accepted"



def freelancer_page():
    zero = 0
    global stored_fren_username
    with open("freelancer_credentials.txt", "r") as f:
        stored_fren_username, stored_password = f.read().split("\n")
        f.close()
        username = stored_fren_username
        print("Hi " + stored_fren_username +" jobs available. Do you want to see the jobs?\n")
        viewjobs = input("(y)es, or (n)o\n")
        if viewjobs == "y":
            with open("jobs.txt", "r") as f:
                job1 = f.read().split("\n")
                job2 = f.read().split("\n")
                job3 = f.read().split("\n")
                job4 = f.read().split("\n")
                job5 = f.read()
                f.close()
                a = [zero, job1, job2, job3, job4, job5]
            print(a[1-6])
        pass
        job_apply = input("Do you want to apply for a (j)ob? or do you want to see job (s)tatus?" + "\n")
        while job_apply == "j":
            i = int(input("Please enter job's number " + "\n"))
            b = (a[i])
            print("Job request sent successfully !")
            break
        while job_apply == "s":
            print("you " + "have been " + str(job_status) + " to your job!" + "\n")
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
