import random

def authenticator():
        print("Use abort to exit the program\n")
        username = input("USERNAME: ")
        if username=="abort":
            print("Have a nice day")
            return
        pin = input("PIN: ")
        pin = int(pin)
        if pin==1234 and username=="user":
            print("\nHello,",username)
            operations()
        else:
            print("ERROR: Invalid authentification\n")
            authenticator()

def operations():
    x = input("Use 1 for math operations, 2 for random facts, 3 to roll the dice, 4 to do the average of some grades, 5 to log out and 6 to exit.\n")
    x = int(x)
    if x==1:
        math_operations()
    if x==2:
        facts()
    if x==3:
        dice()
    if x==4:
        average_Grades()
    if x==5:
        authenticator()
    if x==6:
        print("Have a nice day.")


def math_operations():
    print("\nUse 1 for sum, 2 for substraction, 3 for multiplication, 4 for division and 5 to return to main menu.")
    operation = input("Operation: ")
    operation = int(operation)
    if operation == 1:
        sum()
        math_operations()
    if operation == 2:
        substract()
        math_operations()
    if operation == 3:
        multiplicate()
        math_operations()
    if operation == 4:
        divide()
        math_operations()
    if operation == 5:
        operations()

def sum():
    a = input("\na= ")
    b = input("b= ")
    a = int(a)
    b = int(b)
    s = a+b
    s=int(s)
    print("a+b= ",s)

def substract():
    a = input("\na= ")
    b = input("b= ")
    a = int(a)
    b = int(b)
    sb = a-b
    sb = int(sb)
    print("a-b= ",sb)

def multiplicate():
    a = input("\na= ")
    b = input("b= ")
    a = int(a)
    b = int(b)
    m = a*b
    m = int(m)
    print("a*b= ",m)

def divide():
    a = input("\na= ")
    b = input("b= ")
    a = int(a)
    b = int(b)
    d = a/b
    d = float(d)
    print("a/b= ",d)

def facts():
    fact = [1, 2, 3, 4, 5]
    y = random.choice(fact)
    if y==1:
        print("\nOstriches can run faster than horses, and the males can roar like lions.")
    if y==2:
        print("\nThe bat is the only mammal that can fly.")
    if y==3:
        print("\nThe leg bones of a bat are so thin that no bat can walk.")
    if y==4:
        print("\nThe average fox weighs 14 pounds.")
    if y==5:
        print("\nSome male songbirds sing more than 2000 times each day.")
    x = input("\nUse 1 for another fact, any number to return to main menu\n")
    x = int(x)
    if x==1:
        facts()
    else:
        operations()
        return

def dice():
    face = [1, 2, 3, 4, 5, 6]
    y = random.choice(face)
    print("Dice:",y)
    x = input("\nUse 1 for another roll or any number to return to main menu\n")
    x = int(x)
    if x==1:
        dice()
    else:
        operations()
        return

def average_Grades():
    x = input("Number of grades = ")
    x = int(x)
    average = int(0)
    for i in range(x):
        print("Grade no.",i,": ")
        grade = int(input())
        average+=grade
    average/=x
    sem_test = int(input("Semestrial test(0 means no test) = "))
    if sem_test==0:
        print("The average is ",average)
    else:
	    average*=3
	    average+=sem_test
	    average/=4
	    print("The average is ",average)
    y = int(input("\nUse 1 for another average or any number to return to the main menu\n"))
    if y==1:
        average_Grades()
    else:
        operations()
    
authenticator()
