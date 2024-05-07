import datetime as dt
import random

def one():
    print("--1--")
    day=int(input("Enter day:\n"))
    month=int(input("Enter month:\n"))
    try:
        date=dt.datetime(2024,month,day)
        newyear=dt.datetime(2024,1,1)
        print(date-newyear)
    except:
        print("Invalid date!")
def two():
    print("--2--")
    year1=int(input("Enter first year:\n"))
    month1=int(input("Enter first month:\n"))
    day1=int(input("Enter first day:\n"))

    year2=int(input("Enter second year:\n"))
    month2=int(input("Enter second month:\n"))
    day2=int(input("Enter second day:\n"))
    try:
        firstDate=dt.datetime(year1,month1,day1)
        secondDate=dt.datetime(year2,month2,day2)
        result=firstDate-secondDate
        print(f"years:{int(result.days/365)} months:{int(result.days/30)} days:{int(result.days)}")
    except:
        print("Invalid date!")
def three():
    print("--3--")
    year=int(input("Enter first year:\n"))
    month=int(input("Enter first month:\n"))
    day=int(input("Enter first day:\n"))
    try:
        date=dt.datetime(year,month,day)
        print(date+dt.timedelta(days=60))
    except:
        print("Invlid date!")
def four():
    print("--4--")
    hours=int(input("Enter hours: "))
    minutes=int(input("Enter minutes: "))
    try:
        today=dt.date.today()
        date=dt.datetime(today.year,today.month,today.day,hours,minutes,0)
        newDay=dt.datetime(today.year,today.month,today.day+1,0,0,0)
        print(newDay-date)
    except:
        print("Invalid date!")
def five():
    print("--5--")
    pizzaPrice=10
    colapPrice=3
    pizzaCount=int(input("Enter pizza count:"))
    colaCount=int(input("Enter cola count"))
    if pizzaCount<0 or colaCount<0:
        print("Invalid count!")
    else:
        today=dt.datetime.now()
        delveryDate=dt.datetime(today.year,today.month,today.day,today.hour+2,today.minute,today.second)
        allPrice=pizzaPrice*pizzaCount+colapPrice*colaCount
        print(f"Order will be delivery on {delveryDate.hour}:{delveryDate.minute}")
        print(f"All price is: {allPrice}$")
def six():
    print("--6--")
    won=False
    winNumber=random.randint(0,100)
    for i in range(10):
        num=int(input("Enter number from 1 to 100: "))
        if num>winNumber:
            print("Your number is bigger!")
        elif num<winNumber:
            print("Your number is smaller!")
        elif num==winNumber:
            print("You win!")
            print(f"Win number:{winNumber}")
            won=True
            break
        count+=1
    if not won:
        print("You lost :(")
        print(f"Win number:{winNumber}")
def seven():
    print("--7--")
    num=str(random.randint(1000,9999))
    won=False
    for i in range(10):
        guess=input("Enter number between 1000 and 9999:")
        if guess==num:
            print("You win")
            won=True
            break
        else:
            bulls=0
            cows=0
            for digit in guess:
                if digit in num:
                    if num.index(digit)==guess.index(digit):
                        bulls+=1
                    else:
                        cows+=1
            print(f"bulls:{bulls} cows:{cows}")
    if not won:
        print("You lost :(")
        print(num)
    else:
        print("Congratulations!")
        print(num)
one()
two()
three()
four()
five()
six()
seven()