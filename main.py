import hashlib #مكتبة بتشفر أي حاجة
import os #مكتبة بتقدر تعدل على النظام و تكريت\تمسح فايلات و فولدرات
from os import path #استخدمناها علشان نقدر نوصل لعناوين الفولدرات


#رجاءا لو هتستخدم\ي الكود تدعوا لأخوانكم اللي كاتبين الكود بالتوفيق
#نيتي كانت مساعدة الغير فأرجوا من الله التوفيق


#ترتيب الكود بيكون كالأتي
#1: while loop
#2: signup()
#3: login()
#4: corporation page
#5: freelancer page


def signup(): #بعرف هنا الدالة بتاعة تسجيل الدخول كمستخدم جديد
    status = input("Hi, are you a (f)reelancer or a (c)orporation?" + "\n") #بسأل المستخدم، هل انت شركة ولا فريلانسر؟
    if status == "f":   #لو  هو شركة هيكتب f
        username = input("Enter freelancer username: ")    #باخد منه اليوزرنيم
        email = input("Enter email: ")       #باخد الايميل
        password = input("Enter password: ")     #باخد الباسورد
        while 1:    #عملت لوب و بقوله اني عايزها تشتغل علطول
            conf_pwd = input("Confirm password: ") #باخد منه تأكيد الباسورد
            if conf_pwd == password:  #بقول للأبليكيشن لو الباسورد اتكتب صح مرتين اعمل الآتي
                enc = conf_pwd.encode() #هنا بحدد لكود هيقرا الباسوررد بأنهي طريقة
                hash1 = hashlib.md5(enc).hexdigest() #هنا بيتم تشفير الباسورد 
                with open("./users/usernames.txt", "a")as f: # بفتح فايل و بخزن فيه اليوزرنيمز بس
                    f.write(username + "\n") #بفصل مابين كل يوزرنيم و التاني بسطر فاضي
                    f.close() #بقفل الفايل
                os.mkdir("./users/" + username) # بعمل فولدر باسم اليوزر
                with open("./users/" + username + "/" + username + ".txt", "w")as f: #بفتح الفولدر اللي بإسم اليوزر و بكريت جواه فايل تيكست بإسم اليوزر
                    f.write(username + "\n") #بكتب جوا الفايل اسم اليوزر
                    f.write(hash1) #و بكتب جواه الباسورد
                f.close() #بقفل الفايل
                print("You have registered successfully!")
                break
            else: #هنا لو مدخلش الباسورد صح مرتين
                print("Password is not same as above, please input again. \n")
                #this programme is made by Abdelaziz's team
    elif status == "c": # هنا لو المستخدم شركة هيكتب c
        username = input("Enter corporation username: ") #هاخد منه اليوزرنيم
         #this programme is made by Abdelaziz's team
        email = input("Enter email: ") #هاخد منه الإيميل
        password = input("Enter password: ") #هاخد منه الباسورد
        while 1: #عملت لوب و عايزها تشتغل علطول
            conf_pwd = input("Confirm password: ") #باخد منه تأكيد الباسورد
            if conf_pwd == password: #لو دخل الباسورد صح مرتين اعمل الاتي
                enc = conf_pwd.encode() #حدد طريقة قراية الكود
                hash1 = hashlib.md5(enc).hexdigest() #شفر الباسورد على طريقة md5 
                with open("./users/corp_credentials.txt", "w") as f: #افتح فايل بيتخزن فيه بيانات الشركة
                    f.write(username + "\n") #اكتب اليوزرنيم و بعدين سطر جديد
                     #this programme is made by Abdelaziz's team
                    f.write(hash1) #اكتب الباسورد بعد التشفير
                f.close()
                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again.\n")


def login(): #بعرف دالة تسجيل الدخول
    attempts = 4 #عدد المحاولات بالنسبة لكتابة الباسورد غلط
    global f_username 
    status = input("Are you a (f)reelancer or a (c)orporation?" + "\n") #بسأله انت شركة ولا فريلانسر؟
    if status == "f": #لو فريلانسر
        while attempts >= 0: #اعمل لوب و الشرط بتاعها ان عدد المحاولات يكون اكبر من صفر
            f_username = input("Enter username: ") #خد اليوزرنيم
            password = input("Enter password: ") #و الباسورد
            auth = password.encode() #حدد طريقة القراية
            auth_hash = hashlib.md5(auth).hexdigest() #شفر الباسورد على طريقة md5
            if os.path.isdir("./users/" + f_username): #هنا بقوله لو في فولدر باسم اليوزر (احنا حددنا فوق للكود انه يكريت لكل يوزر جديد فولدر، فابالتالي لو مفيش فولدر باسم اليوزر، فاليوزر متعملش اصلا) اعمل الاتي
                with open("./users/" + f_username + "/" + f_username + ".txt", "r") as f: #افتح فولدر اليوزرز و افتح الفولدر بتاع اليوزر و اقرا الفايل اللي باسم اليوزر
                    stored_f_username, stored_password = f.read().split("\n") #اقرا اليوزرنيم و الباسورد المتخزنين
                    #this programme is made by Abdelaziz's team
                f.close()
                if f_username == stored_f_username and auth_hash == stored_password: #لو اليوزرنيم و الباسورد اللي المستخدم دخلهم هما هما اللي متخزنين اعمل تسجيل الدخول
                    print("Logged in Successfully!")
                    freelancer_page() #افتح صفحة الفريلانسر
                    break
                else:
                    print("Login failed!, you have ", attempts, " attempts to try again\n") #لو مدخلش الباسورد صح
                    attempts = attempts - 1 #قلل عدد المحاولات
            else: #لو مفيش فولدر باسم اليوزر
                print("There is no username like that! please signup!") #قوله انت معملتش يوزر 
                signup()# و افتح صفحة تسجيل يوزر جديد
        if(attempts<0): #لو عدد المحاولات قل عن الصفر
            print("you can't login, try creating account")
            signup() #افتحله صفحة تسجيل يوزر جديد

    elif status == "c": #لو المستخدم شركة، هيدخل c
        #نفس الكود بتاع الفريلانسر اتكرر تاني بالنسبة للشركة
        while attempts >=0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            #this programme is made by Abdelaziz's team
            auth_hash = hashlib.md5(auth).hexdigest()
            with open("./users/corp_credentials.txt", "r") as f: #بس هنا هكتب في فايل واحد عشان الشركة واحدة،ف مش هعمل فايل لكل يوزر
                stored_corp_username, stored_corp_password = f.read().split("\n")
            f.close()
             #this programme is made by Abdelaziz's team
            if username == stored_corp_username and auth_hash == stored_corp_password:
                print("Logged in Successfully!")
                corp_page()
                break
            else:
                print("Login failed!, you have ",attempts," attempts to try again\n")
                attempts=attempts-1
            if attempts < 0:
                cr_account = input(print("you can't login, would try creating an account?"))
                if cr_account == "y":
                    signup()
                else:
                    break

def corp_page(): #بعرف الصفحة بتاعة الشركة
    with open("./users/corp_credentials.txt", "r") as f:
        if not os.path.isfile("./jobs/jobs.txt"):
            with open("./jobs/jobs.txt", "w")as v: #هعمل فايل بخزن فيه اسامي الوظايف اللي الشركة عملتها
                v.close()
                 #this programme is made by Abdelaziz's team
        stored_username, stored_password= f.read().split("\n")
        f.close()
        username = stored_username
        corp_chosen = input("Hi " + username + " Do you want to (l)ist a job or (v)iew applicants?") #هنا بسأل الشركة، هل عايزين يحطوا وظايف جديدة ولا يشوفوا الناس اللي قدمت؟
        if corp_chosen == "l": #لو عايزين يحطوا وظايف جديدة
            num = int(input("Enter number of jobs: ")) #هاخد من الشركة عدد الوظايف
            i = 1 #عداد
            j = 1 #عداد
            while (i<= num and j <= num): #طالما العدادين اقل من عدد الوظايف شغل اللوب
                print("job",i, ":") #اطبع رقم الوظيفة
                title = input("Enter job title: \n") #هاخد اسم الوظيفة
                 #this programme is made by Abdelaziz's team
                id = input("Enter job id: \n") #الاي دي بتاع الوظيفة
                required_skills =input ("Enter required skills: \n") #السكيلز المطلوبة
                job_describ =input("Enter job description: ")# وصف الوظيفة
                with open("./jobs/jobs.txt", "r")as f: #هفتح الفايل اللي كنت خزنت فيه اسامي الوظايف اللي الشركة عملتها
                    xlines = len(f.readlines()) #هقرأ عدد السطور و هخزنه في الفاريابل دا
                    f.close()
                if xlines == 0: #لو عدد السطور صفر(مفيش وظايف اتخزنت)
                    f = open("./jobs/jobs.txt","w") #افتح الفايل
                    f.write(title +"\n") #خزن جواه اول وظيفة و بعدين سطر جديد
                else: #لو في سطور موجودة اصلا
                    f = open("./jobs/jobs.txt", "a") #افتح بطريقة append و حط وظايف زيادة على اللي موجودة اصلا
                    f.write(title + "\n") 
                     #this programme is made by Abdelaziz's team
                if not os.path.isdir("./jobs/" + title): #هنا انا بقوله لو مفيش فولدر للوظيفة اعمل الآتي
                    os.mkdir("./jobs/" + title) #كريت فولدر باسم الوظيفة
                    file_Name = "./jobs/" + title + "/" + title + ".txt" # هنا بحدد عنوان الفايل اللي هيبقى باسم الوظيفة
                    x = open(file_Name, "w") #هنا بقولله يفتحلي الفايل
                    x.write("Title: " + title + "\n") #و يخزن جواه عنوان الوظيفة
                    x.write("id: " + id + "\n") #ال اي دي
                    x.write("Required skills: " + required_skills + "\n") #السكيلز المطلوبة
                    x.write("Job describtion: " + job_describ) #الوصف بتاعها
                    j = j + 1 #زود واحد على العداد
                    i = i + 1 #زود واحد على العداد الاحتياطي
                    #الكود هيقعد يزود واحد على العدادين لحد اما يساووا عدد الوظايف اللي الشركة عايزة تحطها و بعدين اللوب تقف
                else: #هنا بقوله لو في فولدر اصلا للوظيفة (الشركة عاملاها قبل كدا و عايزة تعدل عليها)
                    #هيكرر الكود
                    file_Name = "./jobs/" + title + "/" + title + ".txt"
                    x = open(file_Name, "w")
                    x.write("Title: " + title + "\n")
                    x.write("id: " + id + "\n")
                    x.write("Required skills: " + required_skills + "\n")
                    x.write("Job describtion: " + job_describ)
                    j = j + 1
                    i = i + 1


        elif corp_chosen == "v": # لو الشركة عايزة تشوف الناس اللي قدمت، هتكتب v
            with open("./users/usernames.txt", "r")as f: #هنفتح الفايل اللي متخزن فيه اسامي الناس اللي قدمت على الوظايف
                usernames = f.readlines() #هيقرا السطور
                how_many_usernames = len(f.readlines()) #وبعدين يرجعلي عددهم
                f.close()
            print("Hi, these applicants have applied to a job: \n")
            print(*usernames, sep =", ") #هنا هيطبع اسامي الناس اللي قدمت على الوظايف
            username_chosen = input("Which one do you want to see their application?") #هنا بقول للشركة تدخل اسم الشخص اللي عايزة تشوف المعلومات بتاعته
            user_job_applied = "./users/" + username_chosen + "/" + username_chosen + "_job_applied.txt" #بحدد مكان الفايل اللي هيتخزن فيه الوظيفة اللي الفريلانسر قدم عليها
            user_description = "./users/" + username_chosen + "/" + username_chosen + "_description.txt" #بحدد مكان الفايل اللي بيتكتب فيه الوصف بتاع الفريلانسر
            #this programme is made by Abdelaziz's team
            username_job_status = "./users/" + username_chosen + "/" + username_chosen + "_job_status.txt" #بحدد مكان الفايل اللي هيتخزن فيه هل الفريلانسر اتقبل فالوظيفة ولا لأ
            if os.path.isfile(user_job_applied):  #لو الفايل اللي بيتخزن فيه الوظيفة اللي الشخص قدم عليها موجود اعمل الآتي
                with open(user_job_applied, "r")as f: #هفتح الفايل اللي بيخزن فيه الوظيفة اللي الفريلانسر قدم عليها
                    job_applied = f.read() #و هقرا من جواه اسم الوظيفة اللي قدم عليها
                    f.close()
                with open(user_description, "r")as f: #هفتح الفايل اللي بيتخزن فيه الوصف بتاع الفريلانسر
                    applicant_description = f.read() #و هقرا من جواه الوصف بتاع الفريلانسر
                    f.close()
                print(username_chosen + " has applied to " + job_applied) #هطبعله اسم الفريلانسر و الوظيفة اللي قدم عليها
                 #this programme is made by Abdelaziz's team

                print(username_chosen + "'s bio is: " + "\n" +applicant_description + "\n") #هنا هطبعله الوصف بتاع الفريلانسر
                job_status_1 = input("Wanna accept this application? (y/n): ") #هنا بقول للشركة هل عايزين يقبلوا الفريلانسر ولا لأ
                if job_status_1 == "y": #لو أه
                    job_status = "Accepted"
                    with open(username_job_status, "w") as f:
                        f.write(job_status) #أكتب مقبول جوا الفايل
                        f.close()
                else: #لو لأ
                    job_status = "Not Accepted"
                     #this programme is made by Abdelaziz's team
                    with open(username_job_status, "w") as f:
                        f.write(job_status) #اكتب مش مقبول
                        f.close()
            else: #لو الفايل اللي بيتخزن فيه الوظيفة اللي الشخص قدم عليها مش موجود اعمل الآتي
                print("user has not applied for a job")



def freelancer_page(): #هنا بعرف صفحة الفريلانسر
    zero = 0
    global stored_f_username
    counter = 1 #عداد
    check_job = 0 #فاريابل هنستخدمه لما نسأل الفريلانسر على رقم الوظيفة اللي عايز يشوف معلومات عنها
    lines = 0 #فريابل هيتخزن فيه عدد الوظايف اللي البرنامج طبعها للفريلانسر
    limit = 0 #فاريابل هيتخزن فيه عدد الوظايف اللي متخزنة في الفايل اللي الشركة عملته

    with open("./users/" + f_username + "/" + f_username + ".txt", "r") as f: #هفتح الفايل اللي متخزن فيه اسم الفريلانسر عشان اقرا منه الإسم
        stored_f_username, stored_password = f.read().split("\n")
        f.close()
        username = stored_f_username
        print("Hi " + username + " there are some jobs available. Do you want to see them?\n") #جملة ترحيب
        viewjobs = input("(y)es, or (n)o\n") #هنا بسأله، عايز تشوف الوظايف المتاحة ولا لأ
        if viewjobs == "y": #لو أه
            with open("./jobs/jobs.txt", "r") as f: #هفتح الفايل اللي بيتخزن فيه اسامي الوظايف
                for line in open("./jobs/jobs.txt").readlines(): #و عمل لوب، اللب دي بتقول ان لكل سطر موجود في الملف، هنقرا السطر دا
                    limit+=1 #و بعدين هزود واحد على الفاريابل دا
                job1 = f.read().splitlines() # بعدين هعمل اراي او ليست و هخزن فيها اسامي الوظايف بالترتيب
                 #this programme is made by Abdelaziz's team
                 #في مشكلة هنا، و هي الكود مخزن ترتيب الوظايف في الليستة من اول الزيرو مش الواحد، فأول وظيفة هتبقى الظيفة رقم صفر، و دا هحله تحت
                f.close()
            while lines <= limit-1: #هنا عملت لوب، و الشرط بتاعها ان عدد الوظايف اللي اتطبعت يكون اقل من او يساوي عدد الوظايف اللي متخزنه ناقص واحد (عشان الكود بيبدأعد من الصفر مش الواحد)
                print(counter, ": ", job1[lines],"\n") #هنا الكود هيطبع العداد(اللي بدأناه بواحد) و بعدها هيطبع من الليست job1 الوظيفة رقم lines 
                lines = lines + 1 #زود واحد على عدد الوظايف اللي اتطبعت قدام الفريلانسر
                counter = counter + 1 #زود واحد على عداد رقم الوظيفة(اللي بيظهر قبل اسمها)
            check_job = int(input("Choose a job to see its description, skills needed, and furthermore.\n(Please enter the job's number)\n")) #هنا هقوله اختار رقم الوظيفة اللي عايز تشوف معلومات عنها
            job_num = check_job - 1 #عملت فاريابل بيساوي رقم الوظيفة اللي هو اختارها ناقص واحد (عشان الكود المتخلف بيبدأ عد من الصفر مش الواحد)
            if check_job <= limit: # لو رقم الوظيفة اقل من او يساوي عدد الوظايف اللي متخزنة فالفايل اعمل الآتي
                job_name = job1[job_num] #سجل اسم الوظيفة في الفاريابل دا( الاسم هنقراه من الليستة job1 و هنقرا السطر رقم job_num)
                job_file_name = "./jobs/" + job_name + "/" + job_name + ".txt" #بحدد مكان الفايل بتاع الوظيفة
                with open(job_file_name, "r")as f: #بفتح الفايل على طريقة القراية
                    job_title = f.read().split("\n") #هقرأ عنوان الوظيفة
                    job_id = f.read().split("\n") #الاي دي
                    job_req_skills = f.read().split("\n") #السكيلز المطلوبة
                    job_description = f.read() #الوصف
                    f.close()
                     #this programme is made by Abdelaziz's team
                print(job_title[0] +"\n" + job_title[1] + "\n" + job_title[2] + "\n" + job_title[3]) #هطبع هنا العنوان و الاي دي و السكيلز المطلوبة و الوصف بتاع الوظيفة
            else: #لو الفريلانسر مدخلش رقم وظيفة صح
                print("Please enter a valid number")
        else: #لو الفريلانسر مش عايز يشوف الوظايف المتاحة
            pass #كمل الكود
        job_apply = input("Do you want to apply for a (j)ob? or do you want to see job (s)tatus?" + "\n") #بسأل الفريلانسر، هل عايز يقدم على وظيفة، ولا يشوف هو اتقبل او اترفض؟
        while job_apply == "j": #لو عايز يقدم على وظيفة
            applicant_description = input("Please inter your bio, skills, and social numbers: " + "\n") #هقوله يدخل معلومات عنه(السكيلز بتاعته، رقم تليفونه، وصف عن حياته، كدا)
            applicant_description_file = "./users/" + username + "/" + username + "_description.txt" #هحدد مكان الفايل اللي بيتخزن فيه وصف الفريلانسر
            with open(applicant_description_file, "w")as f: #هفتح الفايل اللي بيخزن فيه وصف الفريلانسر
                f.write(applicant_description + "\n") # و هخزن فيه وصف الفريلانسر
                f.close()
                 #this programme is made by Abdelaziz's team
            i = int(input("Please enter job's number " + "\n")) #هطلب من الفريلانسر رقم الوظيفةاللي قدم عليها
            i_real = i-1 #عملت فاريابل بيساوي رقم الوظيفة اللي الفريلانسر قدم عليها ناقص واحد (عشان الكود المتخلف بيقرا من الصفر مش الواحد)
            job_applied_username = "./users/" + username + "/" + username + "_job_applied.txt" #بحدد مكان الفايل اللي هيتخزن فيه الوظيفة اللي الفريلانسر قدم عليها
            with open("./jobs/jobs.txt", "r")as f: #هفتح الفايل اللي متخزن فيه الوظايف كلها(اللي الشركة عارضاها)
                job_applied_name = f.readlines()[i_real] #و اقرا منه السطر رقم i_real
                f.close()
            with open(job_applied_username, "w")as f: #و هفتح الفايل اللي بيخزن فيه اسم الوظيفة اللي الفريلانسر قدم عليها
                f.write(job_applied_name + "\n") #و هكتب جواه اسم الوظيفة
                f.close()
            print("Job request sent successfully !")
            break
        while job_apply == "s": #لو الفريلانسر عايز يشوف هل هو اتقبل ولا لا
            user_job_status = "./users/" + username + "/" + username +"_job_status.txt" #حددت مكان الفايل اللي بيتخزن فيه هل الفريلانسر اتقبل ولا لأ
            with open(user_job_status, "r") as f: #هفتح الفايل دا
                job_status = f.read() #و اقرا من جواه هل الفريلانسر اتقبل ولا لأ
                f.close()
            print("you " + "have been " + job_status + " to your job!" + "\n") #هطبعله هل هو اتقبل ولا لأ
            break

 #this programme is made by Abdelaziz's team

while 1: #اللوب اللي هتتنفذ اول حاجة
    if not os.path.isdir("users"): #بقوله يتأكد اذا كان الفولدر باسم users موجود ولا لا
        os.mkdir("users") #لو لأ هيكريت الفولدر
    if not os.path.isdir("jobs"): #بتأكد اذا كان الفولدر بأسم jobs موجود ولا لأ
        os.mkdir("jobs") #لو لأ هيكريت الفولدر
         #this programme is made by Abdelaziz's team
    print("\n---------- Login System ----------\n")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
         #this programme is made by Abdelaziz's team
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
