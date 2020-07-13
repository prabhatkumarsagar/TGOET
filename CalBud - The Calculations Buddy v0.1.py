import math
import os
import random
import webbrowser as web
import statistics

def clear():
    if os.name=='nt':
        os.system("cls")
    else:
        os.system("clear")

def pause(stmt):
    try:
        input(stmt)
    except SyntaxError:
        pass

def firstscr():
    clear()
    print("Hey there! Welcome to CalBud, your go to Calculations Buddy, and i am here to make your Calculation Escapades fun and easy. Now before you proceed here are a few things you should know:")
    print("\na) This Program is best run using CMD Shell, so if you want optimum experience and ease while using the program, please use that instead of Python IDLE")
    print("\nb) While performing calculations later in the program, use only numbers in the respective fields and not alphabets or symbols for that might break the program at some instances")
    print("\nc) While performing calculations, the output of your calculation might be printed in floating point numbers with zero after the decimal point rather than in simple integers, but don't they literally mean the same thing? i.e. 5.0 = 5")
    print("\nd) The result of calculations made by this program might not always be 100% correct/accurate as such programs are always prone to errors")
    print("\ne) This Program is meant for personal uses ONLY and no one is to be liable for any fraudulent acts of sorts. Hence, PLEASE USE THE PROGRAM WISELY!")
    pause("\nNow Then, Press ENTER to proceed to the program")
    main()
    
def main():
    while True:
        clear()
        print("So What do you think of doing today?")
        print("1. Some Dull Calculations :D")
        print("2. Get awed with some awesome mathematical facts ;)")
        print("3. Learn mathematics (Requires Internet Access) xD")
        print("0. Exit the program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            cal()
        elif cho=="2":
            rnd_fcts()
        elif cho=="3":
            learn()
        elif cho=="0":
            exit()
        else:
            pause("Invalid Input! Press Enter to retry.")

def cal():
    while True:
        clear()
        print("Very Well! Now then please chose the operation that you're looking for from the following to proceed further..")
        print("\n1. Basic Mathematics -> Addition")
        print("2. Basic Mathematics -> Subtraction")
        print("3. Basic Mathematics -> Multiplication")
        print("4. Basic Mathematics -> Division")
        print("5. Basic Mathematics -> Equations (w/ Various Operators)")
        print("6. Basic Mathematics -> LCM & HCF")
        print("7. Basic Mathematics -> Rounding Numbers")
        print("8. Geometric Operations -> Rectangle")
        print("9. Geometric Operations -> Square")
        print("10. Geometric Operations -> Circle")
        print("11. Geometric Operations -> Triangle")
        print("12. Geometric Operations -> Sphere")
        print("13. Geometric Operations -> Cylinder")
        print("14. Geometric Operations -> Rhombus")
        print("15. Geometric Operations -> Cube")
        print("16. Geometric Operations -> Cuboid")
        print("17. Geometric Operations -> Cone")
        print("18. Everyday Mathematics -> Percentage")
        print("19. Everyday Mathematics -> Power")
        print("20. Everyday Mathematics -> Sqaure Root")
        print("21. Everyday Mathematics -> Units Conversion")
        print("22. Evaluaion Operations -> Prime Numbers")
        print("23. Evaluaion Operations -> Odd/Even")
        print("24. Evaluaion Operations -> Palindrome Numbers")
        print("25. Evaluaion Operations -> Armstrong Numbers")
        print("26. Advanced Mathematics -> Trignometry")
        print("27. Advanced Mathematics -> Statistics")
        print("28. Advanced Mathematics -> Logarithms and Exponents")
        print("#. Return back to the main menu")
        print("0. Exit the Program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            cal_add()
        elif cho=="2":
            cal_sub()
        elif cho=="3":
            cal_mul()
        elif cho=="4":
            cal_div()
        elif cho=="5":
            cal_eqt()
        elif cho=="6":
            cal_lcmhcf()
        elif cho=="7":
            cal_round()
        elif cho=="8":
            cal_geo_rect()
        elif cho=="9":
            cal_geo_sqr()
        elif cho=="10":
            cal_geo_crl()
        elif cho=="11":
            cal_geo_tri()
        elif cho=="12":
            cal_geo_sphr()
        elif cho=="13":
            cal_geo_cln()
        elif cho=="14":
            cal_geo_rhm()
        elif cho=="15":
            cal_geo_cbe()
        elif cho=="16":
            cal_geo_cbd()
        elif cho=="17":
            cal_geo_cone()
        elif cho=="18":
            cal_evd_perc()
        elif cho=="19":
            cal_evd_pow()
        elif cho=="20":
            cal_evd_sqrt()
        elif cho=="21":
            cal_evd_uniconv()
        elif cho=="22":
            cal_eval_prime()
        elif cho=="23":
            cal_eval_evod()
        elif cho=="24":
            cal_eval_pld()
        elif cho=="25":
            cal_eval_arms()
        elif cho=="26":
            cal_trigno()
        elif cho=="27":
            cal_stat()
        elif cho=="28":
            cal_logex()
        elif cho=="#":
            main()
        elif cho=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

def cal_add():
    while True:
        clear()
        print("Alright! Now chose from the following, your next action")
        print("\n1. Addition of two variables")
        print("2. Addition of more than two variables")
        print("#. Return back to the main menu")
        print("0. Exit the Program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            clear()
            try:
                print("Good choice, you know what to do next!")
                x1=eval(input("Enter the First Numeral: "))
                x2=eval(input("Enter the Second Numeral: "))
                print("\n--> The Addition of",x1,"&",x2,"gives",x1+x2)
                pause("Press ENTER to go at it again.")
            except:
                print("Please recheck the values that you've entered!")
                pause("Press ENTER to go at it again.")
        elif cho=="2":
            clear()
            print("Good Choice, now enter the number of terms that you're trying to add!")
            n=int(input("Here: "))
            if n>=2:
                try:
                    smt=0
                    for i in range(n):
                        x=eval(input("Enter the Numeral: "))
                        smt+=x
                    print("\n--> The Addition of the entered numerals gives",smt)
                    pause("Press ENTER to go at it again.")
                except:
                    print("Please recheck the values that you've entered!")
                    pause("Press ENTER to go at it again.")
            else:
                pause("WRONG INPUT! Press ENTER to retry.")
        elif cho=="#":
            main()
        elif cho=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

def cal_sub():
    while True:
        clear()
        print("Alright! Now chose from the following, your next action")
        print("\n1. Subtraction of two variables")
        print("2. Subtraction of more than two variables")
        print("#. Return back to the main menu")
        print("0. Exit the Program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            clear()
            try:
                print("Good choice, you know what to do next!")
                x1=eval(input("Enter the First Numeral: "))
                x2=eval(input("Enter the Second Numeral: "))
                print("\n--> The Subtraction of",x2,"from",x1,"gives",x1-x2)
                pause("Press ENTER to go at it again.")
            except:
                print("Please recheck the values that you've entered!")
                pause("Press ENTER to go at it again.")
        elif cho=="2":
            clear()
            print("Good choice, now enter the number of terms that you wanna perform subtraction upon! (In Order)")
            n=eval(input("Here: "))
            if n>=2:
                try:
                    sub=eval(input("Enter the first Numeral: "))
                    for i in range(n-1):
                        x=eval(input("Enter the next Numeral: "))
                        sub-=x
                    print("\n--> The Subtraction Result of the entered numerals is",sub)
                    pause("Press ENTER to go at it again.")
                except:
                    print("Please recheck the values that you've entered!")
                    pause("Press ENTER to go at it again.")
            else:
                pause("WRONG INPUT! Press ENTER to retry.")
        elif cho=="#":
            main()
        elif cho=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

def cal_mul():
        while True:
            clear()
            print("Alright! Now chose from the following, your next action ")
            print("\n1. Multiplication")
            print("#. Return back to the main menu")
            print("0. Exit the Program")
            cho=input("\nEnter your choice: ")
            if cho=="1":
                clear()
                print("Now to proceed, enter the no. of terms that you want to multiply!")
                n=int(input("Here: "))
                if n>=2:
                    try:
                        mul=1
                        for i in range(n):
                            x=eval(input("Enter the Numeral: "))
                            mul*=x
                        print("\n--> The Multiplication of the entered numerals gives",mul)
                        pause("Press ENTER to go at it again.")
                    except:
                        print("Please recheck the values that you've entered!")
                        pause("Press ENTER to go at it again.")
                else:
                    pause("WRONG INPUT! Press ENTER to retry.")
            elif cho=="#":
                main()
            elif cho=="0":
                exit()
            else:
                pause("WRONG INPUT! Press Enter to retry.")

def cal_div():
        while True:
            clear()
            print("Alright! Now chose from the following, your next action")
            print("\n1. Division")
            print("#. Return back to the main menu")
            print("0. Exit the Program")
            cho=input("\nEnter your choice: ")
            if cho=="1":
                clear()
                try:
                    print("Good choice, you know what to do next!")
                    x1=eval(input("Enter the Dividend(the number which you want to divide): "))
                    x2=eval(input("Enter the Divisor(the number by which you want to divide): "))
                    print("\n--> After dividing",x1,"by",x2,"we get",x1/x2)
                    pause("Press ENTER to go at it again.")
                except:
                    print("Please recheck the values that you've entered!")
                    pause("Press ENTER to go at it again.")
            elif cho=="#":
                main()
            elif cho=="0":
                exit()
            else:
                pause("WRONG INPUT! Press Enter to retry.")


def cal_eqt():
    while True:
        clear()
        print("Alright! Now chose from the following, your next action")
        print("\nNOTE: Use only mathematical numerals and operators while filling the input field. And for Operations such as Multiplication use * (Asterik) instead of x/X and for Exponential(Power) ones use ** (double asterik) e.g. 5*5=25; 5**2=25")
        print("\n1. Numeral Equations (Numbers only, no Variables)")
        print("#. Return back to the main menu")
        print("0. Exit the program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            clear()
            try:
                print("Good choice, now enter your numeral equation")
                n=input("Here: ")
                x=eval(n)
                print("\n--> The Equation",n,"on solving","gives",x)
                pause("Press ENTER to go at it again.")
            except:
                print("Please recheck the values that you've entered!")
                pause("Press ENTER to go at it again.")
        elif cho=="#":
            main()
        elif cho=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")
    
def cal_lcmhcf():
    def hcf(x,y):
        while(y):
            x,y=y,x%y
        return x
    def lcm(x,y):
        lcm=(x*y)//hcf(x,y)
        return lcm
    while True:
        clear()
        print("Alright! Now chose from the following, your next action")
        print("\n1. LCM of two numbers")
        print("2. HCF of two numbers")
        print("#. Return back to the main menu")
        print("0. Exit the program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            clear()
            try:
                print("Alright LCM it is!")
                l=eval(input("Enter the first numeral: "))
                c=eval(input("Enter the second numeral: "))
                m=lcm(l,c)
                print("\n--> The LCM of",l,'&',c,"is",m)
                pause("Press ENTER to go at it again.")
            except:
                print("Please recheck the values that you've entered!")
                pause("Press ENTER to go at it again.")
        elif cho=="2":
            clear()
            try:
                print("Alright HCM it is!")
                h=eval(input("Enter the first numeral: "))
                c=eval(input("Enter the second numeral: "))
                f=hcf(h,c)
                print("\n--> The HCF of",h,'&',c,"is",f)
                pause("Press ENTER to go at it again.")
            except:
                print("Please recheck the values that you've entered!")
                pause("Press ENTER to go at it again.")
        elif cho=="#":
            main()
        elif cho=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

def cal_round():
    while True:
        clear()
        print("Alright Rounding here we go!")
        print("\n1. Rounding Digits (Integers/Floating Point/..)")
        print("#. Return back to the main menu")
        print("0. Exit the program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            clear()
            try:
                x=eval(input("Enter the number to be rounded: "))
                n=eval(input("Enter the number of digits up to which the given number is to be rounded:"))
                z=round(x,n)
                print("\n--> The rounded off number is",z)
                pause("Press ENTER to go at it again.")
            except:
                print("Please recheck the values that you've entered!")
                pause("Press ENTER to go at it again.")
        elif cho=="#":
            main()
        elif cho=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_rect():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    l=eval(input("Enter the Length of the Rectangle(in metres): "))
    b=eval(input("Enter the Breadth(Width) of the Rectangle(in metres): "))
    print("\n1. AREA")
    print("2. PERIMETER")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        r=l*b
        print("\n--> The Area of the given Rectangle(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=2*(l+b)
        print("\n--> The Perimeter of the given Rectangle(in metres) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_sqr():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    s=eval(input("Enter the side of the Square(in metres): "))
    print("\n1. AREA")
    print("2. PERIMETER")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        r=s**2
        print("\n--> The Area of the given Square(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=4*s
        print("\n--> The Perimeter of the given Square(in metres) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_crl():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    R=eval(input("Enter the radius of the Circle(in metre): "))
    s=input("Enter the length of the arc of the Circle(in metres)(FOR SECTOR *OPTIONAL:): ")
    a=input("Enter the chord length of the Circle(in metres)(FOR SEGMENT *OPTIONAL): ")
    h=input("Enter the height of the segment of the Circle(in metres)(FOR SEGMENT *OPTIONAL): ")
    print("\n1. AREA OF A CIRCLE")
    print("2. PERIMETER/CIRCUMFERENCE OF A CIRCLE")
    print("3. AREA OF A SECTOR")
    print("4. PERIMETER/CIRCUMFERENCE OF A SECTOR")
    print("5. AREA OF A SEGMENT")
    print("6. PERIMETER/CIRCUMFERENCE OF A SEGMENT")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        r=math.pi*(R**2)
        print("\n--> The Area of the given Circle(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=2*math.pi*R
        print("\n--> The Perimeter of the given Circle(in metres) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="3":
        s=int(s)
        r=(R*s)/2
        print("\n--> The Area of the given Sector(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="4":
        s=int(s)
        r=s+(2*R)
        print("\n--> The Perimeter of the given Sector(in metres) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="5":
        s=int(s)
        a=int(a)
        h=int(h)
        r=1/2*((s*R)-a*(R-h))
        print("\n--> The Area of the given Segment(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="6":
        s=int(s)
        a=int(a)
        r=s+a
        print("\n--> The Perimeter of the given Segment(in metres) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_tri():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    a=eval(input("Enter the first side of the Triangle(in metres): "))
    b=eval(input("Enter the second side of the Triangle(in metres): "))
    c=eval(input("Enter the third side of the Triangle(in metres): "))
    print("\n1. AREA")
    print("2. PERIMETER")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        s=(a+b+c)/2
        r=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("\n--> The Area of the given Triangle(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=a+b+c
        print("\n--> The Perimeter of the given Triangle(in metres) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_sphr():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    R=eval(input("Enter the radius of the Sphere(in metres): "))
    print("\n1. SURFACE AREA")
    print("2. VOLUME")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        r=4*math.pi*(R**2)
        print("\n--> The Surface Area of the given Sphere(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=4/3*math.pi*(R**3)
        print("\n--> The Volume of the given Sphere(in metre cb) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")    

def cal_geo_cln():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    R=eval(input("Enter the radius of the Cylinder(in metres): "))
    H=eval(input("Enter the height of the Cylinder(in metres): "))
    print("\n1. TOTAL SURFACE AREA")
    print("2. LATERAL SURFACE AREA")
    print("3. VOLUME")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        r=2*math.pi*R*(H+R)
        print("\n--> The Total Surface Area of the given Cylinder(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=2*math.pi*R*H
        print("\n--> The Lateral Surface Area of the given Cylinder(in metre sq) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="3":
        r=math.pi*(R**2)*H
        print("\n--> The Volume of the given Cylinder(in metre cb) is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_rhm():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    a=eval(input("Enter the length of the Rhombus(in metres): "))
    h=eval(input("Enter the height of the Rhombus(in metres): "))
    print("\n1. AREA")
    print("2. PERIMETER")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
         r=a*h
         print("\n--> The Area of the given Rhombus(in metre sq) is",r)
         pause("Press ENTER to go at it again.")
    elif cho2=="2":
         r=4*a
         print("\n--> The Perimeter of the given Rhombus(in metres) is",r)
         pause("Press ENTER to go at it again.")
    elif cho2=="#":
         return
    else:
         pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_cbe():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    s=eval(input("Enter the side of the Cube(in metres): "))
    print("\n1. TOTAL SURFACE AREA OF THE CUBE")
    print("2. LATERAL SURFACE AREA OF THE CUBE")
    print("3. VOLUME OF THE CUBE")
    print("4. PERIMETER OF THE CUBE")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        r=6*(s**2)
        print("\n--> The Total Surface Area(in metre sq) of the given Cube is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=4*(s**2)
        print("\n--> The Lateral Surface Area(in metre sq) of the given Cube is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="3":
        r=s**3
        print("\n--> The Volume(in metre cb) of the given Cube is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="4":
        r=12*s
        print("\n--> The Perimeter(in metres) of the given Cube is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_cbd():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    a=eval(input("Enter the length of the Cuboid(in metres): "))
    b=eval(input("Enter the breadth(width) of the Cuboid(in metres): "))
    c=eval(input("Enter the height of the Cuboid(in metres): "))
    print("\n1. TOTAL SURFACE AREA OF THE CUBOID")
    print("2. LATERAL SURFACE AREA OF THE CUBOID")
    print("3. VOLUME OF THE CUBOID")
    print("4. PERIMETER OF THE CUBOID")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        r=2*(a*b+b*c+a*c)
        print("\n--> The Total Surface Area(in metre sq) of the given Cuboid is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=2*c*(a+b)
        print("\n--> The Lateral Surface Area(in metre sq) of the given Cuboid is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="3":
        r=a*b*c
        print("\n--> The Volume(in metre cb) of the given Cuboid is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="4":
        r=4*(a+b+c)
        print("\n--> The Perimeter(in metres) of the given Cuboid is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_geo_cone():
    clear()
    print("Right! Now fill the following details and chose which operation you wanna perform!")
    R=eval(input("Enter the radius of the Cone(in metres): "))
    l=eval(input("Enter the slant(genaratrix) height of the Cone(in metres): "))
    H=eval(input("Enter the height of the Cone(in metres): "))
    print("\n1. TOTAL SURFACE AREA OF THE CONE")
    print("2. LATERAL SURFACE AREA OF THE CONE")
    print("3. VOLUME OF THE CONE")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        r=math.pi*R*(l+R)
        print("\n--> The Total Surface Area(in metre sq) of the given Cone is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        r=math.pi*R*l
        print("\n--> The Lateral Surface Area(in metre sq) of the given Cone is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="3":
        r=(math.pi)/3*(R**2)*H
        print("\n--> The Volume(in metre sq) of the given Cone is",r)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_evd_perc():
    clear()
    print("Alright! Now which type of percentage operation do you wanna perform!")
    print("\n1. Percentage Finder (X is what Percentage of Y e.g. 5 is '50%' of 10)")
    print("2. Number Finder (What is X Percentage of Y e.g. 50% of 10 is '5')")
    print("#. Return back to the main menu")
    cho2=input("\nEnter your choice: ")
    if cho2=="1":
        x=eval(input("Enter the Number whose percentage you wanna derive(X): "))
        y=eval(input("Enter the Number from which you're deriving the percentage(Y): "))
        z=x/y*100
        print("\n--> The Result of the calculation shows:",x,"is",z,"%","of",y)
        pause("Press ENTER to go at it again.")
    elif cho2=="2":
        x=eval(input("Enter the Percentage(X): "))
        y=eval(input("Enter the Number(Y): "))
        z=(y/100)*x
        print("\n--> The Result of the calculation shows:",x,"% of",y,"is",z)
        pause("Press ENTER to go at it again.")
    elif cho2=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry.")

def cal_evd_pow():
    clear()
    print("Alright! Powers it is!")
    try:
        x=int(input("Enter the Base Number(whose power you wanna find): "))
        y=int(input("Enter the Power Number(upto which the base number will be be raised): "))
        z=math.pow(x,y)
        print("\n-->",x,"raised to the power",y,"gives",z)
        pause("Press ENTER to go back to the previous screen.")
    except:
        print("Make sure you've entered the values correctly mate!")
        pause("Press ENTER to retry.")

def cal_evd_sqrt():
    clear()
    print("Alright! Now enter the element whose Square Root you wanna find!")
    try:
        x=int(input("Here: "))
        y=math.sqrt(x)
        print("\n--> The Square Root of the",x,"is",y)
        pause("Press ENTER to go back to the previous screen.")
    except:
        print("Make sure you've entered the values correctly mate!")
        pause("Press ENTER to retry.")


def cal_evd_uniconv():
    clear()
    print("Alright! Now chose from the following which type of unit conversion you wanna perform!")
    print("\n1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    print("3. Kilometres to Miles")
    print("4. Miles to Kilometres")
    print("5. Feets to Metres")
    print("6. Metres to Feets")
    print("7. Kilograms to Pounds")
    print("8. Pounds to Kilogram")
    print("9. Inches to Centimetres")
    print("10. Centimetres to Inches")
    print("11. Litres to Gallons")
    print("12. Gallons to Litres")
    print("#. Return back to the previous menu")
    print("0. Exit the program")
    cho=input("\nEnter your choice: ")
    if cho=="1":
        x=eval(input("Enter the Temperature in Celcius: "))
        y=(x*(9/5))+32
        print("The Temperature in Fahrenheit Scale is",y)
        pause("Press Enter to go at it again")
    elif cho=="2":
        x=eval(input("Enter the Temperature in Fahrenheit: "))
        y=(x-32)*5/9
        print("The Temperature in Celcius Scale is",y)
        pause("Press Enter to go at it again")
    elif cho=="3":
        x=eval(input("Enter the Length in Kilometres: "))
        y=x/1.609
        print("The Length in Miles is",y)
        pause("Press Enter to go at it again")
    elif cho=="4":
        x=eval(input("Enter the Length in Kilometres: "))
        y=x*1.609
        print("The Length in Kilometres is",y)
        pause("Press Enter to go at it again")
    elif cho=="5":
        x=eval(input("Enter the Length in Foot/Feet: "))
        y=x/3.281
        print("The Length in Metres is",y)
        pause("Press Enter to go at it again")
    elif cho=="6":
        x=eval(input("Enter the Length in Metres: "))
        y=x*3.281
        print("The Length in Foot/Feet is",y)
        pause("Press Enter to go at it again")
    elif cho=="7":
        x=eval(input("Enter the Mass in Kilogram: "))
        y=x*2.205
        print("The Mass in Pounds is",y)
        pause("Press Enter to go at it again")
    elif cho=="8":
        x=eval(input("Enter the Mass in Pounds: "))
        y=x/2.205
        print("The Mass in Kilograms is",y)
        pause("Press Enter to go at it again")
    elif cho=="9":
        x=eval(input("Enter the Length in Inches: "))
        y=x*2.54
        print("The Length in Centimetres is",y)
        pause("Press Enter to go at it again")
    elif cho=="10":
        x=eval(input("Enter the Length in Centimetres: "))
        y=x/2.54
        print("The Length in Inches is",y)
        pause("Press Enter to go at it again")
    elif cho=="11":
        x=eval(input("Enter the Volume in Litres: "))
        y=x*3.785
        print("The Volume in Gallons is",y)
        pause("Press Enter to go at it again")
    elif cho=="12":
        x=eval(input("Enter the Volume in Gallons: "))
        y=x/3.785
        print("The Volume in Litres is",y)
        pause("Press Enter to go at it again")
    elif cho=="#":
        return
    else:
        pause("WRONG INPUT! Press Enter to retry")

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
  

def cal_eval_prime():
    clear()
    print("Alright! Now enter the number you wanna check for Prime!")
    try:
        p=int(input("Enter the Number: "));
        z=isPrime(p)
        if z==False:
            print("No,",p,"is not a Prime Number!");
            pause("Press Enter to go at it again")
            return
        else:
            print("Yes,",p,"is a Prime Number!");
            pause("Press Enter to go at it again")
            return
    except:
        pause("WRONG INPUT! Press Enter to retry")


def cal_eval_evod():
    clear()
    print("Alright! Now enter the number you wanna check for Even or Odd!")
    try:
        num=int(input("Here: "));
        if (num % 2) == 0:
            print(num,"is an Even Number")
            pause("Press Enter to go at it again")
        else:
            print(num,"is an Odd Number")
            pause("Press Enter to go at it again")
    except:
        pause("WRONG INPUT! Press Enter to retry")

def cal_eval_pld():
    clear()
    print("Alright! Now enter the number you wanna check for Palindrome!")
    try:
        num=int(input("Here: "))
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            print("YES the entered number is palindrome!")
            pause("Press Enter to go at it again")
        else:
            print("NO the entered number is Not a palindrome!")
            pause("Press Enter to go at it again")
    except:
        pause("WRONG INPUT! Press Enter to retry")

def cal_eval_arms():
    clear()
    print("Alright! Now enter the number you wanna check for Armstrong!")
    try:
        num = int(input("Here: "))
        sum = 0
        temp = num
        while temp > 0:
           digit = temp % 10
           sum += digit ** 3
           temp //= 10
        if num == sum:
           print("YES",num,"is an Armstrong number")
           pause("Press Enter to go at it again")
        else:
           print("NO",num,"is not an Armstrong number")
           pause("Press Enter to go at it again")
    except:
        pause("WRONG INPUT! Press Enter to retry")            
            
def cal_stat():
    while True:
        clear()
        print("Alright! Now firstly enter the no. of elements there are in the list of numbers and then the numbers themselves, one after another, upon which you wanna perform statistical operations!")
        try:
            n=int(input("Here: "))
            l=[]
            for i in range(n):
                x=int(input("Element: "))
                l.append(x)
        except:
            pause("WRONG INPUT! Press Enter to retry")     
        print("\n1. MEAN")
        print("2. MEDIAN")
        print("3. MODE")
        print("4. STANDARD DEVIATION")
        print("5. VARIANCE")
        print("#. Return back to the main menu")
        print("0. Exit the program")
        cho2=input("\nEnter your choice: ")
        if cho2=="1":
            y=statistics.mean(l)
            print("\n--> The Mean of the given list of numbers is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="2":
            y=statistics.median(l)
            print("\n--> The Median of the given list of numbers is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="3":
            y=statistics.mode(l)
            print("\n--> The Mode of the given list of numbers is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="4":
            y=statistics.stdev(l)
            print("\n--> The Standard Deviation of the given list of numbers is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="5":
            y=statistics.variance(l)
            print("\n--> The Varaince in the given list of numbers is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="#":
            cal()
        elif cho2=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

def cal_trigno():
    while True:
        clear()
        print("Alright! Now enter the angle(in degrees) upon which you wanna perform trignometric operations(OPTIONAL; Press Enter to skip!)!")
        a=str(input("Here: "))
        print("\nNow Chose from the following what you'd like to do next!")
        print("1. Sine of this angle")
        print("2. Cosine of this angle")
        print("3. Tangent of this angle")
        print("a. Degrees to Radians Conversion")
        print("b. Radians to Degrees Conversion")
        print("#. Return back to the main menu")
        print("0. Exit the program")
        cho2=input("\nEnter your choice: ")
        if cho2=="1":
            a=int(a)
            y=math.sin(math.radians(a))
            print("\n--> The Sine(sin) of the given angle",a,"is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="2":
            a=int(a)
            y=math.cos(math.radians(a))
            print("\n--> The Cosine(cos) of the given angle",a,"is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="3":
            a=int(a)
            y=math.tan(math.radians(a))
            print("\n--> The Tangent(tan) of the given angle",a,"is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="a":
            x=eval(input("Enter the Angle in Degrees: "))
            y=math.radians(x)
            print("\n--> On conversion",x,"in radians is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="b":
            x=eval(input("Enter the Angle in Radians: "))
            y=math.degrees(x)
            print("\n--> On conversion",x,"in degrees is",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="#":
            cal()
        elif cho2=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

def cal_logex():
    while True:
        clear()
        print("Alright! Now chose from the following which logarithmic/exponential operation you wanna perform!")
        print("\n1. Natural Log (base e)")
        print("2. Log2 (base 2)")
        print("3. Log10 (base 10)")
        print("4. Log(a,b) (any base of your choice (b))")
        print("5. Exponential raised to a power")
        print("#. Return back to the main menu")
        print("0. Exit the program")
        cho2=input("\nEnter your choice: ")
        if cho2=="1":
            x=eval(input("Enter the numeral(a): "))
            y=math.log(x)
            print("\n--> Log",x,"returns",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="2":
            x=eval(input("Enter the numeral(a): "))
            y=math.log2(x)
            print("\n--> Log base 2",x,"returns",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="3":
            x=eval(input("Enter the numeral(a): "))
            y=math.log10(x)
            print("\n--> Log base 10",x,"returns",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="4":
            x=eval(input("Enter the numeral(a): "))
            b=eval(input("Enter the base(b): "))
            y=math.log(x,b)
            print("\n--> Log base",b,x,"returns",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="5":
            x=eval(input("Enter the numeral(to whose power you wanna raise e): "))
            y=math.exp(x)
            print("\n--> e raised to the power",x,"returns",y)
            pause("Press ENTER to go back to the previous screen.")
        elif cho2=="#":
            cal()
        elif cho2=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")


def rnd_fcts():
    l=["The word \"hundred\" comes from the old Norse term, \"hundrath\", which actually means 120 and not 100.","In a room of 23 people there’s a 50% chance that two people have the same birthday.","Most mathematical symbols weren’t invented until the 16th century. Before that, equations were written in words.","\"Forty\" is the only number that is spelt with letters arranged in alphabetical order.","\"One\" is the only number that is spelt with letters arranged in descending order.",
       "From 0 to 1000, the only number that has the letter \"a\" in it is \"one thousand\".","'Four’ is the only number in the English language that is spelt with the same number of letters as the number itself.","Every odd number has an \"e\" in it.","The reason Americans call mathematics \"math\", is because they argue that \"mathematics\" functions as a singular noun so ‘math’ should be singular too.","Markings on animal bones indicate that humans have been doing maths since around 30,000BC.","\"Eleven plus two\" is an anagram of \"twelve plus one\" which is pretty fitting as the answer to both equations is 13.","Zero is not represented in Roman numerals.",
       "2 and 5 are the only prime numbers that end in 2 or 5.","A ‘jiffy’ is an actual unit of time. It means 1/100th of a second.","555 is used by some in Thailand as slang for \"hahaha\", because the word for \"five\" is pronounced \"ha\"","10! seconds is exactly 6 weeks.","Cicadas use prime numbers as an evolutionary strategy.",".999999... = 1","(6 × 9) + (6 + 9) = 69.","111,111,111 × 111,111,111 = 12,345,678,987,654,321.",
       "A pizza that has radius \"z\" and height \"a\" has volume Pi × z × z × a.","The number 4 is considered unlucky in much of Asia.","Zero is an even number.","If you write out pi to two decimal places, backwards it spells \"pie\". i.e 3.14 (backwards) = PIE","A French word for pie chart is \"camembert\".","We tend to think of odd numbers as male and even numbers as female.",
       "The Fibonacci sequence is encoded in the number 1/89.","The spiral shapes of sunflowers follow a Fibonacci sequence.","If you shuffle a deck of cards properly, it’s more than likely that the exact order of the cards you get has never been seen before in the whole history of the universe.","The most popular favourite number is 7. That might be because 7 is \"arithmetically unique\".","The word \"mathematics\" only appears in one Shakespearean play, \"The Taming of the Shrew\".","The symbol for division (i.e.÷) is called an obelus.","-40 °C is equal to -40 °F."]
       
    while True:
        clear()
        fact=random.choice(l)
        print("Here goes! :D\n")
        print(fact)
        print("\nBet you didn't know that! What Next?")
        print("1. Another supercalifragilisticexpialidocious Fact")
        print("#. Return back to the main menu")
        print("0. Exit the program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            continue
        elif cho=="#":
            main()
        elif cho=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

def learn():
    while True:
        clear()
        print("\"Pure mathematics is, in its own way, the poetry of logical ideas.\" ~ Albert Einstein")
        print("\nLearn Basic and Advanced Mathematics, free of cost and hand in hand with your grade, with the help of these Gems aka Websites.")
        print("\nNote: You will need a stable internet connection to access these sites and once you do, chose either of the following sites but keep in mind that you will be redirected to a New Tab on your default Web Browser in doing so.")
        print("\n1. Khan Academy (Kindergarten,Grades 1-12,SAT & many other test prep courses)")
        print("2. Cliffs Notes (2nd grade through College,SAT and other higher maths courses)")
        print("3. SumDog (Kindergarten through 8th Grade)")
        print("#. Return back to the previous menu")
        print("0. Exit the program")
        cho=input("\nEnter your choice: ")
        if cho=="1":
            print("Happy Learning!")
            web.open('https://www.khanacademy.org',new=0,autoraise=True)
        elif cho=="2":
            print("Happy Learning!")
            web.open('https://www.cliffsnotes.com',new=0,autoraise=True)
        elif cho=="3":
            print("Happy Learning!")
            web.open('https://www.sumdog.com',new=0,autoraise=True)
        elif cho=="#":
            main()
        elif cho=="0":
            exit()
        else:
            pause("WRONG INPUT! Press Enter to retry.")

firstscr()
