import math as m
def one():
    print("--1--")
    a=int(input("Enter side:"))
    h=int(input("Enter height:"))
    def area(a,h):
        if a<0 or h<0:
            return -1
        else:
            result=(a*h)/2
            return result
    print(area(a,h))

def two():
    print("--2--")
    x1=int(input("Enter coord1 x:"))
    y1=int(input("Enter coord1 y:"))
    x2=int(input("Enter coord2 x:"))
    y2=int(input("Enter coord2 y:"))
    def calcDistance(x1,y1,x2,y2):
        distance=m.sqrt(m.pow(y2-y1,2)+m.pow(x2-x1,2))
        return distance
    print(calcDistance(x1,y1,x2,y2))

def three():
    print("--3--")
    fname=input("Enter first name:")
    lname=input("Enter last name:")
    age=int(input("Enter age:"))
    position=input("Enter position:")
    def printEmployee(fname,lname,age,position):
        if age<0:
           print("Invalid age!")
           return
        print(f"Name: {fname} {lname}")
        print(f"Age: {age}")
        print(f"Position: {position}")
    printEmployee(fname,lname,age,position)

def four():
    print("--4--")
    days=int(input("Enter days:"))
    beds=int(input("Enter beds:"))
    tickets=int(input("Enter tickets:"))
    def calcPrice(days,beds,tickets):
        bedPrice=15
        return days*beds*15+tickets*2
    print(calcPrice(days,beds,tickets))

def five():
    print("--5--")
    pizzaPrice=int(input("Enter pizza price:"))
    pizzaCount=int(input("Enter pizza count:"))
    drinkPrice=int(input("Enter drink price:"))
    drinkCount=int(input("Enter drinkCount count:"))
    def calcPrice(pizzaPrice,pizzaCount,drinkPrice,drinkCount):
        if pizzaPrice<0 or pizzaCount<0 or drinkPrice<0 or drinkPrice<0:
            print("Invalid data!")
            return
        deliveryPrice=7
        print(pizzaPrice*pizzaCount+drinkPrice*drinkCount+deliveryPrice)
    calcPrice(pizzaPrice,pizzaCount,drinkPrice,drinkCount)

def six():
    print("--6--")
    p=int(input("Enter first number:"))
    q=int(input("Enter second number:"))
    def makeEquation(p,q):
        print(f"x^2-{p+q}x+{p*q}x")
    makeEquation(p,q)

def seven():
    print("--7--")
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=int(input("Enter three number:"))
    def checkP(a,b,c):
      if m.pow(c,2)==m.pow(a,2)+m.pow(b,2):
          return True
      else:
          return False
    print(checkP(a,b,c))

def eight():
    print("--8--")
    list1=[2,1,4,5,7]
    list2=[4,1,3,4,6]
    def checkAverage(list1,list2):
        avgList1=sum(list1)/len(list1)
        avgList2=sum(list2)/len(list2)
        if avgList2==avgList1:
            return True
        else:
            return False
    print(checkAverage(list1,list2))

def nine():
    print("--9--")
    string=input("Enter word:")
    def crypt(string):
        result=""
        for i in range(len(string)):
          code=ord(string[i])
          code+=2
          result+=chr(code)
        return result
    print(crypt(string))

def ten():
    print("--10--")
    n=int(input("Enter number:"))
    def fb(n):
       if n==1 or n==2 or n==3:
           return 1
       else:
           return fb(n-1)+fb(n-2)+fb(n-3)
    print(fb(6))
one()
two()
three()
four()
five()
six()
seven()
eight()
nine()
ten()
