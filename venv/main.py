import sqlConection
import sys
#main
def menu():
    quit = 0;
    while (quit == 0):
        print()
        print("************MAIN MENU**************")
        print()

        choice = input("""
                              A: פונקציה שיוצרת שיחה חדשה.
                              B: פונקציה שמציגה את כל השיחות של לקוח לפי מספר טלפון.
                              C: פונקציה שמציגה את הסכום לתשלום של לקוח לכל הקווים שלו לפי ת"ז.
                              D: פונקציה שבודקת את מספר הקווים לכל מסלול.
                              E: פונקציה שבודקת קו האם חרג ממספר הדקות המותר.
                              F: Quit/Log Out

                              Please enter your choice: """)

        if choice == "A" or choice == "a":
           sqlConection.addTalking()
        elif choice == "B" or choice == "b":
            phone=input("enter your phone")
            sqlConection.getTalkingByPhone(phone)
        elif choice == "C" or choice == "c":
            code = input("enter your code")
            sqlConection.getcost(code);
        elif choice == "D" or choice == "d":
            sqlConection.getCountLinesOfAnyRoute()
        elif choice == "E" or choice == "e":
            phone = input("enter your phone")
            sqlConection.exceptionCheck(phone)
        elif choice == "F" or choice == "f":
            print("יציאה                              ")
            quit = 1;
            sys.exit
        else:
            print("You must only select either A,B,C,D or E.")


menu()