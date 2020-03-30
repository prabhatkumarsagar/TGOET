#LIBRARY MANAGEMENT PROGRAM(Using Python & MySQL) *Made by Prabhat Kumar Sagar and Anirban Dutta (Students of Kendriya Vidyalaya Malda) **Under the Guidance of - Mr. Tanmay Suhaneimport getpass
import getpass
import mysql.connector as sql
import webbrowser as w3 
import os
available=True
try:
    import tabulate as tbl
except:
    available=False

def pause(st):
    try:
        input(st)
    except SyntaxError:
        pass
    
def clr():
    if os.name=='nt':
        os.system("cls")#for windows terminal
    else:
        os.system("clear")#for linux terminal

while True:
        try:
            u=input("\n Enter MySQL Username(\'root\' by default, just press enter): ")
            if u=='':
                u='root'
            p=input(" Enter MySQL Password: ")
            con = sql.connect(host="127.0.0.1",user=u,passwd=p)
            break
        
        except:
            print("\n Could not Connect to MySQL at this Moment. Make sure the same is Installed Properly alongwith the Python Connector or, Just Look for the Username/Password.")
cur=con.cursor()

#1. Structure and Base Portion!
def tb_construct():
    cur.execute("create table if not exists passwrd(S_No int(1),Password varchar(30));")
    cur.execute("create table if not exists Books(LUID varchar(10), Name varchar(100), Author varchar(30), ISBN varchar(30), Publisher varchar(50), Genre varchar(50), Date_Added date, Availability char(1) DEFAULT 'Y', CONSTRAINT book_luid_pk PRIMARY KEY(LUID));")
    cur.execute("create table if not exists Articles(LUID varchar(10), Name varchar(100), Author varchar(30), Vendor varchar(50), Date_Added date, Availability char(1) DEFAULT 'Y', CONSTRAINT art_luid_pk PRIMARY KEY(LUID));")
    cur.execute("create table if not exists Archives(LUID varchar(10), Name varchar(100), Author varchar(30), Vendor varchar(50), Date_Added date, Availability char(1) DEFAULT 'Y', CONSTRAINT arc_luid_pk PRIMARY KEY(LUID));")
    cur.execute("create table if not exists issue_req_book(S_No int(50) PRIMARY KEY auto_increment, Name varchar(30), LUID varchar(10), Name_Apc varchar(50), UID_Apc varchar(50) default('Teacher'), CONSTRAINT bk_luid_fk FOREIGN KEY (LUID) REFERENCES Books(LUID));")
    cur.execute("create table if not exists issue_req_article(S_No int(50) PRIMARY KEY auto_increment, Name varchar(30), LUID varchar(10), Name_Apc varchar(50), UID_Apc varchar(50) default('Teacher'), CONSTRAINT art_luid_fk FOREIGN KEY (LUID) REFERENCES Articles(LUID));")
    cur.execute("create table if not exists issue_req_archive(S_No int(50) PRIMARY KEY auto_increment, Name varchar(30), LUID varchar(10), Name_Apc varchar(50), CONSTRAINT arc_luid_fk FOREIGN KEY (LUID) REFERENCES Archives(LUID));")
    cur.execute("create table if not exists issue_his_book(S_No int(50) PRIMARY KEY auto_increment, LUID varchar(10), Apc_Name varchar(50), uid varchar(10), issue_date date, return_date date, CONSTRAINT bkhis_luid_fk FOREIGN KEY (LUID) REFERENCES books(LUID));")
    cur.execute("create table if not exists issue_his_article(S_No int(50) PRIMARY KEY auto_increment, LUID varchar(10), Apc_Name varchar(50), uid varchar(10), issue_date date, return_date date, CONSTRAINT arthis_luid_fk FOREIGN KEY (LUID) REFERENCES articles(LUID));")
    cur.execute("create table if not exists issue_his_archive(S_No int(50) PRIMARY KEY auto_increment, LUID varchar(10), Apc_Name varchar(50), uid varchar(10), issue_date date, return_date date, CONSTRAINT archis_luid_fk FOREIGN KEY (LUID) REFERENCES archives(LUID));")

def valid(st):
    upr=0
    lwr=0
    dgt=0
    for i in st:
        if i.isdigit():
            dgt+=1
        elif i.isupper():
            upr+=1
        elif i.islower():
            lwr+=1
    a=0
    if len(st)<8:
        print("\n Failed length validation. Allowed length: (>= 8)")
        a+=1
    if upr<1:
        print("\n Failed uppercase validation. (A - Z)")
        a+=1
    if lwr<1:
        print("\n Failed lower case validation. (a - z)")
        a+=1
    if dgt<1:
        print("\n Failed integer validation. Allowed integers: (0 - 9)")
        a+=1
    if a>0:
        return False
    else:
        print("\n Password validated successfully.")
        return True

def dispData(data,Column_list):
    if len(data)==0:
        print("\n NO DATA AVAILABLE!")
    else:
        if available:
            print(tbl.tabulate(data,headers=Column_list))
        else: 
            a=0
            for row in data:
                for i in row:
                    print(Column_list[a],':',i, end=' | ')
                    a+=1
                print('\n')
                a=0
            print("\n NOTE: For this Program to work as intended i.e flawlessly, you need to Install the Python Tabulate Module, which can be done using the following syntax:- \n\n python -m pip install tabulate \n\n Typecast this in the CMD Shell and that's it! and Once you have it Installed Please Try Re-running the Program! If you're not able to  do so, then the program will still work but with an old outlook.")
    return
        
def pswd():    
    cur.execute("create database if not exists Lib_Management;")
    cur.execute("use Lib_Management;")
    p3 = ""
    tb_construct()
    while(True):
        p3=input('\n Enter the New Password (Make Sure it consists of 1 Upper-Case letter,\n 1 Lower-Case letter,1 Digit and is of atleast 8 characters!): ') 
        if valid(p3):
            s=1
            cur.execute("insert into passwrd(S_No,Password) values(%i,'%s');"%(s,p3))
            con.commit()
            break
        else:
            print("\n The password that you entered does not meet the required criterion!\n Please try again.")
            continue

def menu():
    clr()
    print("\n Welcome to the Library Management System 0.5 of Kendriya Vidyalaya Malda!")
    print("\n\n Before you dive into the Program here are a few things you should know about:")
    print(" a. This Program was Made for Experimental Purposes only and Kendriya Vidyalaya  Malda is not Liable for its use, in any way.")
    print(" b. The Functions/Commands you Perform here are Stored on this     and only this Specific Machince.")
    print(" c. In Case of Inputing Data, which is the often occuring case, if you're trying to enter data containing special chars like - '-:/%\" please use escape \n sequence '\\' before the text in order to not break the program and cause an\n error.")
    print(" d. If You're an Admin and you're Using CMD Shell then note that- while \n logging-in, the password will not be echoed/printed on screen. Just typecast\n the password and Hit Enter.")
    pause("\n Now that you know that, let's get you back to the Main Program!\n\n Press Enter to Proceed.")
    while(True):
        clr()
        print("\nLibrary Management>>")
        print("\n 1. To Enter the Program")
        print(" O. To Exit the Program")
        choice=input("\n Enter your CHOICE:: ")
        if(choice=='1'):    
                dsg=input("\n To Proceed Further Please Enter Your Designation \n (For Admin - ADM, For Student User - STU, For Teacher User - TCHR):: ")
                dsg=dsg.lower()
                if dsg=='adm':
                    if admLogin():
                        admMenu()
                elif dsg=='stu':
                    stuMenu()                    
                elif dsg=='tchr':
                    teaMenu()
                else:
                    pause("\n Invald Designation Entered! Please press Enter to Try Again.")            
                continue

        if choice=="0":
            exit()
            
        else: 
            pause("\n INVALID INPUT! Press Enter to Try Again")
            continue

def admLogin():
        clr()
        print("\nLibrary Management>>Admin Login")
        bln=True
        while(bln):
            try:
                cur.execute("use Lib_Management;")
                cur.execute("select Password from passwrd where S_No=1;")
                data=cur.fetchall()
                p2=""
                for i in data:
                    for j in i:
                        p2=j
            
                if p2=="": 
                    bln=False
                    continue
                print('\n Hello Admin, To Get Going Please Enter Your User Credentials, i.e ')
                pas=getpass.getpass('\n Password: ')
                if pas==p2:
                    pause("\n Hey There Admin, now that we know it's you, let's get going!\n\n Press Enter to Proceed ;)")
                    return True
     
                else:
                     print("\n Looks Like the Entered Password is Incorrect, Let's Try Again")
                     continue
            except:
              print()
              pswd()
        else:
          pause("\n Something Seems to be wrong, please try again by creating a new password! \n Press Enter to Proceed.\n")
          pswd()
          bln=True

#2. Content and the Base 2 Portion!
def admMenu():
   while(True):
        clr()
        print("\nLibrary Management>>Admin's Section>>")
        print("\n Welcome to the Administration Interface.")
        print("\n 1. To View and Edit the Books Catalogue.")
        print(" 2. To View and Edit the Articles Catalogue.")
        print(" 3. To View and Edit the Archives Catalogue.")
        print(" 4. To View the Issue Requests.")
        print(" 5. To Return Items back to Library's Catalogue.")
        print(" 6. To Grant Issue Requests.")
        print(" 7. To See Past Issue Records")
        print(" 8. To Change Admin Password.")
        print(" 0. To Return back to the Previous Menu.")
        print(' #. To Exit the Program.')
        cho=input("\n What do you think of doing today? Enter the CHOICE:: ")
        if cho=='1':
            clr()
            editMenuBooks()
            continue

        if cho=='2':
            clr()
            editMenuArticles()
            continue

        if cho=='3':
            clr()
            editMenuArchives()
            continue
                    
        if cho=='4':
            clr()
            viewIssueRequests()
            continue

        if cho=="5":
            clr()
            returnItems()
            continue
        
        if cho=="6":
            clr()
            grantIssues()
            continue

        if cho=="7":
            clr()
            print("\nLibrary Management>>Admin's Section>>Issues Register>>")
            issueHistory()
            continue
        
        if cho=="8":
            clr()
            print("\nLibrary Management>>Admin's Section>>Change Admin Password>>")
            print("\n Changing your Password right away! \n But first please re-enter your previous password")
            if admLogin():
                print('\n Enter the New Password (Make Sure it consists of 1 Upper-Case letter,\n 1 Lower-Case letter,1 Digit and is of atleast 8 characters) ')
                pas=input(" Here : ")
                if valid(pas):
                    cur.execute("update passwrd set Password='%s' where S_No=1;"%pas)
                    con.commit()
                    print("\n And is Now Changed! Remember it while logging-in the next time. \n Let's get you back to the Admin UI!")
                else:
                    print('  The new password that you entered does not meet the required criterion!\n Please try again.')
            pause('\n Press Enter to Continue')
            continue
        
        if cho=="0":
            return 

        if cho=='#':
            exit()
        
        else:
            pause("\n INVALID INPUT! Press Enter to Try Again")
            continue

def stuMenu():
    while(True):
        clr()
        try:
            cur.execute("use Lib_Management;")
        except:
            print(" The Program is Broken i.e Incomplete! Please contact your Librarian.\n The reason for this might be the Absence of Initial Data Modelling by the Same.")
            return
        print("\nLibrary Management>>Student's Section>>")
        print("\n Welcome Student!")
        print("\n 1. Browse the Books Catalogue.")
        print(" 2. Browse Articles/Magazines.")
        print(" 3. Browse Online Scholastic-Study Materials.")
        print(" 4. Make an Issue-Request.")
        print(" 5. Return Pre-Issued Items.")
        print(" 0. Return back to the Previous Menu.")
        print(' #. Exit the Program.')
    
        choice=input("\n What are you upto today? Enter the CHOICE:: ")

        if choice=='1':
            clr()
            print("\nLibrary Management>>Student's Section>>Books Catalogue")
            print("\n List of all the available Books in the Library\n")
            cur.execute("select LUID,Name,Author,ISBN,Publisher,Genre,Date_added from Books where Availability='Y';")
            data=cur.fetchall()
            dispData(data,('LUID','Book Name','Author','ISBN','Publisher','Genre','Date Added'))
            pause('\n Press Enter to Continue')
            continue

        if choice=='2':
            clr()
            print("\nLibrary Management>>Student's Section>>Article Catalogue")
            print("\n List of all the available Articles in the Library\n")
            cur.execute("select LUID,Name, Author,Vendor,Date_added from Articles where Availability='Y';")
            data=cur.fetchall()
            dispData(data,('LUID','Article Name','Author','Vendor','Date Added'))
            pause('\n Press Enter to Continue')
            continue

        if choice=='3':
            clr()
            print("\nLibrary Management>>Student's Section>>Online Study Materials>>")
            viewMenuSM()
            continue
                    
        if choice=='4':
            clr()
            print("\nLibrary Management>>Student's Section>>Issue Request>>")
            issueReqStu()
            continue
            
        if choice=='5':
            clr()
            print("\nLibrary Management>>Student's Section>>Return Item>>")
            print("\n In Order to Return an Issued Item, you need to contact the Librarian in-person. We Cannot Help you in this Case.")
            pause('\n Press Enter to Continue')
            continue

        if choice=="0":
            return

        if choice=="#":
            exit()

        else:
            pause("\n INVALID INPUT! Press Enter to Continue")
            continue

def teaMenu():
    while(True):
        clr()
        try:
            cur.execute("use Lib_Management;")
        except:
            print(" The Program is Broken i.e Incomplete! Please contact the Librarian.\n *The reason for this might be the Absence of Initial Data Modelling by the Same.")
            return
        print("\nLibrary Management>>Teacher's Section>>")
        print("\n Welcome Teacher!")
        print("\n 1. Browse the Books Catalogue.")
        print(" 2. Browse Articles/Magazines.")
        print(" 3. Browse KV Archives.")
        print(" 4. Browse Online Student's Study Materials.")
        print(" 5. Make an Issue-Request.")
        print(" 6. Return Pre-Issued Item(s).")
        print(" 0. Return back to the Previous Menu.")
        print(' #. Exit the Program.')
        
        choice=input("\n How can we help you today, Teacher? Enter the CHOICE:: ")

        if choice=='1':
            clr()
            print("\nLibrary Management>>Teacher's Section>>Book Catalogue")
            print("\n List of all the available Books in the Library\n")
            cur.execute("select LUID,Name,Author,ISBN,Publisher,Genre,Date_added from Books where Availability='Y';")
            data=cur.fetchall()
            dispData(data,('LUID','Book Name','Author','ISBN','Publisher','Genre','Date Added'))
            pause('\n Press Enter to Continue')
            continue
       
        if choice=='2':
            clr()
            print("\nLibrary Management>>Teacher's Section>>Article Catalogue")
            print("\n List of all the available Articles in the Library\n")
            cur.execute("select LUID,Name, Author,Vendor,Date_added from Articles where Availability='Y';")
            data=cur.fetchall()
            dispData(data,('LUID','Article Name','Author','Vendor','Date Added'))
            pause('\n Press Enter to Continue')
            continue

        if choice=='3':
            clr()
            print("\nLibrary Management>>Teacher's Section>>Archive Catalogue")
            print("\n List of all the available Archives in the Library\n")
            cur.execute("select LUID,Name, Author,Vendor,Date_added from Archives where Availability='Y';")
            data=cur.fetchall()
            dispData(data,('LUID','Archive Name','Author','Vendor','Date Added'))
            pause('\n Press Enter to Continue')
            continue

        if choice=='4':
            clr()
            print("\nLibrary Management>>Teacher's Section>>Online Study Materials>>")
            viewMenuSM()
            continue
                    
        if choice=='5':
            clr()
            print("\nLibrary Management>>Teacher's Section>>Issue Request>>")
            issueReqTea()
            continue
            
        if choice=='6':
            clr()
            print("\nLibrary Management>>Teacher's Section>>Return Item>>")
            print("\n In Order to Return an Issued Item, you need to contact the Librarian in-person. We Can't Help you in this Case.")
            pause('\n Press Enter to Continue')
            continue

        if choice=="0":
            return

        if choice=="#":
            exit()

        else:
            pause("\n INVALID INPUT! Press Enter to Continue.")
            continue


#3. Definitions and actual Programmed Part!
def viewIssueRequests():
    print("\nLibrary Management>>Admin's Section>>Issue Requests>>")
    z1=input("\n What Category Issue Requests are you Looking For? \n ('B' for Boooks, 'Art' for Articles, 'Arc' for Archives): ")
    if z1.lower()=='b':
        cur.execute("select * from issue_req_book order by s_no;")
        data=cur.fetchall()
        print("\n The Pending Issue Requests for Books are:\n ")
        column=('SNO','Book Name','LUID','Appicant Name','Applicant ID')
        dispData(data,column)
    elif z1.lower()=='art':
        cur.execute("select s_no,name,luid,name_apc,uid_apc from issue_req_article order by s_no;")
        data=cur.fetchall()
        print("\n The Pending Issue Requests for Articles are:\n ")
        column=('SNO','Article Name','LUID','Appicant Name','Applicant ID')
        dispData(data,column)
    elif z1.lower()=='arc':
        cur.execute("select s_no,name,luid,name_apc from issue_req_archive order by s_no;")
        data=cur.fetchall()
        print("\n The Pending Issue Requests for Archives are:\n ")
        column=('SNO','Archive Name','LUID','Appicant Name')
        dispData(data,column)
    else:
        print("\n INVALID INPUT!")
    pause('\n Press Enter to Continue')
    return

def editMenuBooks():
    while(True):
        clr()
        print("\nLibrary Management>>Admin's Section>>Books>>")
        print("\n *. To See Pre-Existing Books in the Catalogue.")
        print(" 1. To Create New Entries.")
        print(' 2. To Update an Existing Entry.')
        print(" 3. To Delete an Entry.")
        print(" 0. To Return back to the Previous Menu.")
        
        choice=input("\n Enter your CHOICE:: ")

        if choice=='*':
            clr()
            print("\nLibrary Management>>Admin's Section>>Books>>Books List")
            cur.execute("select * from Books;")
            data=cur.fetchall()
            print("\n List of All Pre-Existing Books in the Library is as Follows\n ")
            dispData(data,('LUID','Book Name','Author','ISBN','Publisher','Genre','Date Added','Available'))
            pause('\n Press Enter to Continue')
            continue

        if choice=='1':
            clr()
            print("\nLibrary Management>>Admin's Section>>Books>>New Entry")
            a1=input("\n Enter the Library Unique ID(LUID): ")
            a2=input(" Enter the Name of the Book: ")
            a3=input(" Enter the ISBN: ")
            a4=input(" Enter the Author\'s Name: ")
            a5=input(" Enter the Publisher\'s Name: ")
            a6=input(" Enter the Genre: ")
            try:
                cur.execute("insert into Books(LUID,Name,ISBN,Author,Publisher,Genre,Date_Added) values('%s','%s','%s','%s','%s','%s',curdate());"%(a1,a2,a3,a4,a5,a6))
                con.commit()
                print("\n Record Added Successfully!")
            except:
                print("\n Data error!\n The data you entered does not comply to the fore-mentioned guidelines! Please try again.")
            pause('\n Press Enter to Continue')
            continue

        if choice=='2':
            clr()
            print("\nLibrary Management>>Admin's Section>>Books>>Update Entry")
            f=input("\n Enter the Field to Update: ")
            a=input(" Enter the Old Value: ")
            b=input(" Enter the New Value: ")
            f=f.lower()
            if f=="book name":
                f='name'
            if f=='date added':
                f='date_added'
            try:
                cur.execute("update books set %s='%s' where %s='%s';"%(f,b,f,a))
                con.commit()
                print("\n Record Updated Successfully!")
            except:
                print("\n Data error!\n The data you entered does not comply to the fore-mentioned guidelines! Please try again.")
            pause('\n Press Enter to Continue')
            continue

        if choice=="3":
            clr()
            print("\nLibrary Management>>Admin's Section>>Books>>Delete Entry")
            d=input("\n Enter the LUID of the Book you want to Delete: ")
            try:
                cur.execute("delete from books where luid='%s';"%(d))
                con.commit()
                print("\n Record Deleted Successfully!")
            except:
                print('\n No Book found with a matching LUID!\n Please enter a valid LUID.')
            pause('\n Press Enter to Continue')
            continue
                
        if choice=="0":
            return

        else:
            pause("\n INVALID INPUT! Press Enter to Try Again")
            continue

def editMenuArticles():
    while(True):
        clr()
        print("\nLibrary Management>>Admin's Section>>Articles>>")
        print("\n *. To See Pre-Existing Articles in the Catalogue.")
        print(" 1. To Create New Entries.")
        print(" 2. To Update an Existing Entry.")
        print(" 3. To Delete an Entry.")
        print(" 0. To Return back to the Previous Menu.")
        
        choice=input("\n Enter your CHOICE:: ")

        if choice=='*':
            clr()
            print("\nLibrary Management>>Admin's Section>>Articles>>Article List")
            cur.execute("select * from Articles;")
            data=cur.fetchall()
            print("\n List of All Pre-Existing Articles in the Library is as Follows\n ")
            dispData(data,('LUID','Article Name','Author','Vendor','Date Added','Available'))
            pause('\n Press Enter to Continue')
            continue

        if choice=='1':
            clr()
            print("\nLibrary Management>>Admin's Section>>Articles>>New Entry")
            b1=input("\n Enter the Library Unique ID: ")
            b2=input(" Enter the Name of the Article: ")
            b3=input(" Enter the Author\'s Name: ")
            b4=input(" Enter the Vendor\'s Name: ")
            try:
                cur.execute("insert into Articles(LUID,Name,Author,Vendor,Date_added) values('%s','%s','%s','%s',curdate());"%(b1,b2,b3,b4))
                con.commit()
                print("\n Record Added Successfully!")
            except:
                print("\n Data error!\n The data you entered does not comply to the fore-mentioned guidelines! Please try again.")
            pause('\n Press Enter to Continue')
            continue

        if choice=='2':
            clr()
            print("\nLibrary Management>>Admin's Section>>Articles>>Update Entry")
            f=input("\n Enter the Field to Update: ")
            a=input(" Enter the Old Value: ")
            b=input(" Enter the New Value: ")
            f=f.lower()
            if f=="article name":
                f='name'
            if f=='date added':
                f='date_added'
            try:
                cur.execute("update articles set %s='%s' where %s='%s';"%(f,b,f,a))
                con.commit()
                print("\n Record Updated Successfully!")
            except:
                print("\n Data error!\n The data you entered does not comply to the fore-mentioned guidelines! Please try again.")
            pause('\n Press Enter to Continue')
            continue

        if choice=="3":
            clr()
            print("\nLibrary Management>>Admin's Section>>Articles>>Delete Entry")
            d=input("\n Enter the LUID of the Article you wanna Delete: ")
            try:
                cur.execute("delete from articles where luid='%s';"%(d))
                con.commit()
                print("\n Record Deleted Successfully!")
            except:
                print('\n No Article found with a matching LUID!\n Please enter a valid LUID.')
            pause('\n Press Enter to Continue')
            continue

        if choice=="0":
            return

        else:
            pause("\n INVALID INPUT! Press Enter to Try Again")
            continue

def editMenuArchives():
    while(True):
        clr()
        print("\nLibrary Management>>Admin's Section>>Archives>>")
        print("\n *. To See Pre-Existing Archives in the Catalogue.")
        print(" 1. To Create New Entries.")
        print(" 2. To Update an Existing Entry.")
        print(" 3. To Delete an Entry.")
        print(" 0. To Return back to the Previous Menu.")
        
        choice=input("\n Enter your CHOICE: ")

        if choice=='*':
            clr()
            print("\nLibrary Management>>Admin's Section>>Archives>>Archive List")
            cur.execute("select * from Archives;")
            data=cur.fetchall()
            print("\n List of All Pre-Existing Archives in the Library is as Follows\n")
            dispData(data,('LUID','Archive Name','Author','Vendor','Date Added','Available'))
            pause('\n Press Enter to Continue')
            continue

        if choice=='1':
            clr()
            print("\nLibrary Management>>Admin's Section>>Archives>>New Entry")
            c1=input("\n Enter the Library Unique ID: ")
            c2=input(" Enter the Name of the Archive: ")
            c3=input(" Enter the Author\'s Name: ")
            c4=input(" Enter the Vendor Name: ")
            try:
                cur.execute("insert into Archives(LUID,Name,Author,Vendor,Date_added) values('%s','%s','%s','%s',curdate());"%(c1,c2,c3,c4))
                con.commit()
                print("\n Record Added Successfully!")
            except:
                print("\n Data error!\n The data you entered does not comply to the fore-mentioned guidelines! Please try again.")
            pause('\n Press Enter to Continue')
            continue

        if choice=='2':
            clr()
            print("\nLibrary Management>>Admin's Section>>Archives>>Update Entry")
            f=input("\n Enter the Field to Update: ")
            a=input(" Enter the Old Value: ")
            b=input(" Enter the New Value: ")
            f=f.lower()
            if f=="archive name":
                f='name'
            if f=='date added':
                f='date_added'
            try:
                cur.execute("update archives set %s='%s' where %s='%s';"%(f,b,f,a))
                con.commit()
                print("\n Record Updated Successfully!")
            except:
                print("\n Data error!\n The data you entered does not comply to the fore-mentioned guidelines! Please try again.")
            pause('\n Press Enter to Continue')
            continue
        
        if choice=="3":
            clr()
            print("\nLibrary Management>>Admin's Section>>Archives>>Delete Entry")
            d=input(" Enter the LUID of the Archive you want to Delete: ")
            try:
                cur.execute("delete from archives where luid='%s';"%(d))
                con.commit()
                print("\n Record Deleted Successfully!")
            except:
                print('\n No Article found with a matching LUID!\n Please enter a valid LUID.')
            pause('\n Press Enter to Continue')
            continue
        
        if choice=="0":
            return

        else:
            pause("\n INVALID INPUT! Press Enter to Try Again")
            continue


def viewMenuSM():
    while(True):   
        print("\n 1. To Visit the School Website and Access Available Study Material.\n 2. To Visit the School's Literature Blog.\n 0. To Return back to Previous Menu.\n #. To Exit.")
        sm=input("\n Enter your CHOICE:: ")
        if sm=='1':
            print(" Here you go!")
            w3.open('https://nhpcmalda.kvs.ac.in/school-strengthening-vidyalayas/library-e-granthalaya', new=0, autoraise=True)
            continue
        if sm=='2':
            print(' Here you go!')
            w3.open('https://kvmaldalitclub.blogspot.com/', new=0, autoraise=True)
            continue
        if sm=='0':
            return
        if sm=='#':
            exit()
        

def issueReqStu():
    isr=input("\n What do you want to Issue('B' for Book, 'Art' for Article): ")
    isr = isr.lower()
    if isr=='b':
        clr()
        print("\nLibrary Management>>Student's Section>>Issue Request>>Book(s)")
        x1=input('\n Enter the Name of the Applicant:: ')
        x2=input(' Enter the UID of the Applicant:: ')
        x3=input(' Enter the Name of the Book:: ')
        x4=input(' Enter the Library Unique Identity(LUID) of the Book:: ')
        try:
            cur.execute("insert into issue_req_book(Name_Apc,UID_Apc,Name,LUID) values('%s','%s','%s','%s');"%(x1,x2,x3,x4))
            con.commit()
            print('\n Your Issue Request has been Submitted and is now awaiting approval from the\n Admin. It Usually takes 24 hours, so hold onto your Horses! ;)')
            pause("\n Press Enter to Continue")
        except:
            print("\n We are not able to Process your Request at this Moment. \n Make Sure the Data you've Entered is Valid and then try again.")
            pause("\n Press Enter to Continue")
        return

    if isr=='art':
        clr()
        print("\nLibrary Management>>Student's Section>>Issue Request>>Article(s)")
        x5=input('\n Enter the Name of the Applicant:: ')
        x6=input(' Enter the Admission No of the Applicant:: ')
        x7=input(' Enter the Name of the Article/Magazine:: ')
        x8=input(' Enter the Library Unique Identity(LUID) of the Article/Magazine:: ')
        try:
            cur.execute("insert into issue_req_article(Name_Apc,UID_Apc,Name,LUID) values('%s','%s','%s','%s');"%(x5,x6,x7,x8))
            con.commit()
            print('\n Your Issue Request has been Submitted and is now awaiting approval from the\n Admin. It Usually takes 24 hours, so hold onto your Horses! ;)')
            pause("\n Press Enter to Continue")
        except:
            print("\n We are not able to Process your Request at this Moment.\n Make Sure the Data you've Entered is Valid and then try again.")
            pause("\n Press Enter to Continue")
            return
    else:
        print("\n INVALID INPUT!")
        return
    pause('\n Press Enter to Continue')

def issueReqTea():
    isr2=input("\n What do you want to Issue('B' for Book, 'Art' for Article, 'Arc' for Archive): ")
    isr2=isr2.lower()
    if isr2=='b':
        clr()
        print("\nLibrary Management>>Teacher's Section>>Issue Request>>Book(s)")
        k1=input('\n Enter the Name of the Applicant:: ')
        k2=input(' Enter the Name of the Book:: ')
        k3=input(' Enter the Library Unique Identity(LUID) of the Book:: ')
        try:
            cur.execute("insert into issue_req_book(Name_Apc,Name,LUID) values('%s','%s','%s');"%(k1,k2,k3))
            con.commit()
            print('\n Your Issue Request has been Submitted and is now awaiting approval from the\n Admin. It Usually takes 24 hours, so hold onto your Horses! ;)')
            pause("\n Press Enter to Continue")
        except:
            print("\n We are not able to Process your Request at this Moment.\n Make Sure the Data you've Entered is Valid and then try again.")
            pause("\n Press Enter to Continue")
            return
    if isr2=='art':
        clr()
        print("\nLibrary Management>>Teacher's Section>>Issue Request>>Article(s)")
        k4=input('\n Enter the Name of the Applicant:: ')
        k5=input(' Enter the Name of the Article/Magazine:: ')
        k6=input(' Enter the Library Unique Identity(LUID) of the Article/Magazine:: ')
        try:
            cur.execute("insert into issue_req_article(Name_Apc,Name,LUID) values('%s','%s','%s');"%(k4,k5,k6))
            con.commit()
            print('\n Your Issue Request has been Submitted and is now awaiting approval from the\n Admin. It Usually takes 24 hours, so hold onto your Horses! ;)')
            pause("\n Press Enter to Continue")
        except:
            print("\n We are not able to Process your Request at this Moment.\n Make Sure the Data you've Entered is Valid and then try again.")
            pause("\n Press Enter to Continue")
            return
    if isr2=='arc':
        clr()
        print("\nLibrary Management>>Teacher's Section>>Issue Request>>Archive(s)")
        k7=input('\n Enter the Name of the Applicant:: ')
        k8=input(' Enter the Name of the Archive:: ')
        k9=input(' Enter the Library Unique Identity(LUID) of the Archive:: ')
        try:
            cur.execute("insert into issue_req_archive(Name_Apc,Name,LUID) values('%s','%s','%s');"%(k7,k8,k9))
            con.commit()
            print('\n Your Issue Request has been Submitted and is now awaiting approval from the\n Admin. It Usually takes 24 hours, so hold onto your Horses! ;)')
            pause("\n Press Enter to Continue")
        except:
            print("\n We are not able to Process your Request at this Moment.\n Make Sure the Data you've Entered is Valid and then try again.")
            pause("\n Press Enter to Continue")
            return
    else:
        print("\n INVALID INPUT!")
        return
    pause('\n Press Enter to Continue')


def returnItems():
    while(True):
        clr()   
        print("\nLibrary Management>>Admin's Section>>Return Items>>") 
        print("\n What do you want to Return?")
        print(" 1. Book")
        print(" 2. Article")
        print(" 3. Archive")
        print(" 0. To Return back to the Previous Menu")
        a=input(" Enter your CHOICE: ")
        if a=='1':
            clr()
            print("\nLibrary Management>>Admin's Section>>Return Items>>Book(s)")
            u1=input("\n Enter the LUID of the Book you want to Return: ")
            try:
                cur.execute("update books set availability='Y' where LUID='%s';"%(u1))
                cur.execute("update issue_his_book set return_date=curdate() where LUID='%s';"%(u1))
                con.commit()
                print("\n Book returned to the Library successfully!")
            except:
                print("\n We are not able to Process your Request at this Moment. Please Try Again Later")
            pause('\n Press Enter to Continue')
            continue
        if a=='2':
            clr()
            print("\nLibrary Management>>Admin's Section>>Return Items>>Article(s)")
            u1=input("\n Enter the LUID of the Article you want to Return: ")
            try:
                cur.execute("update article set availability='Y' where LUID='%s';"%(u1))
                cur.execute("update issue_his_article set return_date=curdate() where LUID='%s';"%(u1))
                con.commit()
                print("\n Article returned to the library successfully!")
            except:
                print("\n We are not able to Process your Request at this Moment. Please Try Again Later")
            pause('\n Press Enter to Continue')
            continue
        if a=='3':
            clr()
            print("\nLibrary Management>>Admin's Section>>Return Items>>Achive(s)")
            u1=input("\n Enter the LUID of the Archive you want to Return: ")
            try:
                cur.execute("update archive set availability='Y' where LUID='%s';"%(u1))
                cur.execute("update issue_his_archive set return_date=curdate() where LUID='%s';"%(u1))
                con.commit()
                print("\n Archive returned to the library successfully!")
            except:
                print("\n We are not able to Process your Request at this Moment. Please Try Again Later")
            pause('\n Press Enter to Continue')    
            continue
        if a=='0':
            return
        else:
            pause("\n INVALID INPUT! Press Enter to Try Again")
            continue

def grantIssues():
    while(True):
        clr()
        print("\nLibrary Management>>Admin's Section>>Granting Issues>>")
        print("\n 1. To Grant a Book")
        print(" 2. To Grant an Article")
        print(" 3. To Grant an Archive")
        print(" 0. To Return back to the Previous Menu")
        choice=input("\n Enter your CHOICE: ")
        if choice=='1':
            clr()
            print("\nLibrary Management>>Admin's Section>>Granting Issues>>Book(s)")
            nm=input("\n Enter the Name of the applicant: ")
            ui=input(" If Student- Enter Adm.No; If Teacher- Typecast 'TCHR': ")
            if ui.isalpha():
                ui.lower()
            luid=input(" Enter the LUID of the Book: ")
            try:
                cur.execute("insert into issue_his_book(LUID,apc_name,uid,issue_date) values('%s','%s','%s',curdate());"%(luid,nm,ui))
                cur.execute("update books set availability='N' where LUID='%s';"%(luid))
                cur.execute("delete from issue_req_book where LUID='%s';"%(luid))
                con.commit()
                print("\n Issue Request Granted Successfully!")
            except:
                print("\n We are not able to Process your Request at this Moment. Please Try Again Later")
            pause('\n Press Enter to Continue')
            continue
            
        if choice=='2':
            clr()
            print("\nLibrary Management>>Admin's Section>>Granting Issues>>Article(s)")
            nm=input("\n Enter the Name of the applicant: ")
            ui=input(" If Student- Enter Adm.No; If Teacher- Typecast 'TCHR': ")
            if ui.isalpha():
                ui.lower()
            luid=input(" Enter the LUID of the Article: ")
            try:
                cur.execute("insert into issue_his_article(LUID,apc_name,uid,issue_date) values('%s','%s','%s',curdate());"%(luid,nm,ui))
                cur.execute("update articles set availability='N' where LUID='%s';"%(luid))
                cur.execute("delete from issue_req_article where LUID='%s';"%(luid))
                con.commit()
                print("\n Issue Request Granted Successfully!")
            except:
                print("\n We are not able to Process your Request at this Moment. Please Try Again Later")
            pause('\n Press Enter to Continue')    
            continue 

        if choice=='3':
            clr()
            print("\nLibrary Management>>Admin's Section>>Granting Issues>>Issue Archive")
            nm=input("\n Enter the Name of the Applicant: ")
            ui=input(" If Student- Enter Adm.No; If Teacher- Typecast 'TCHR': ")
            if ui.isalpha():
                ui.lower()
            luid=input(" Enter the LUID of the Archive: ")
            try:
                cur.execute("insert into issue_his_archive(LUID,apc_name,uid,issue_date) values('%s','%s','%s',curdate());"%(luid,nm,ui))
                cur.execute("update archives set availability='N' where LUID='%s';"%(luid))
                cur.execute("delete from issue_req_archive where LUID='%s';"%(luid))
                con.commit()
                print("\n Issue Request Granted Successfully!")
            except:
                print("\n We are not able to Process your Request at this Moment. Please Try Again Later")
            pause('\n Press Enter to Continue')
            continue  
        
        if choice=='0':
            return
            
        else:
            pause("\n INVALID INPUT! Press Enter to Try Again")   
            continue

def issueHistory():
        cho=input("\n What Category Issue Records are you Looking For?\n ('B' for Books; 'Art' for Articles; 'Arc' for Archives :: ")
        cho=cho.lower()
        if cho=='b':
                clr()
                print("\nLibrary Management>>Admin's Section>>Issue Register>>Book(s)")
                print("\n List of all the Books Issued in the Past is as follows \n")
                cur.execute("select * from issue_his_book order by s_no;")
                data=cur.fetchall()
                column=('LUID','Appicant Name','Unique ID','Issue Date','Return Date')
                dispData(data,column)
                pause("\n Press Enter to Continue")
                return

        if cho=='art':
                clr()
                print("\nLibrary Management>>Admin's Section>>Issue Register>>Article(s)")
                print("\n List of all the Articles Issued in the Past is as follows \n")
                cur.execute("select * from issue_his_article order by s_no;")
                data=cur.fetchall()
                column=('LUID','Appicant Name','Unique ID','Issue Date','Return Date')
                dispData(data,column)
                pause("\n Press Enter to Continue")
                return

        if cho=='arc':
                clr()
                print("\nLibrary Management>>Admin's Section>>Issue Register>>Archive(s)")
                print("\n List of all the Archives Issued in the Past is as follows \n")
                cur.execute("select * from issue_his_archive order by s_no;")
                data=cur.fetchall()
                column=('LUID','Appicant Name','Unique ID','Issue Date','Return Date')
                dispData(data,column)
                pause("\n Press Enter to Continue")
                return

        else:
            pause("\n INVALID INPUT! Press Enter to Try Again")   
            return
        
#4. Final Calling Part!
menu()
