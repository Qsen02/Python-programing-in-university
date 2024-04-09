import math as m
def one():
    print("--1--")
    month=int(input("Enter month:\n"))
    months=[31,28,31,30,31,30,31,30,31,31,30,31]
    print(months[month-1])

def two():
    print("--2--")
    n=int(input("Enter number:"))
    if n<=9:
      for i in range(1,11):
        print(f"{n}*{i}={n*i}")
    else:
        print("Number must be between 1 and 9!")

def three():
     print("--3--")
     a=int(input("Enter a:\n"))
     b=int(input("Enter b:\n"))
     c=int(input("Enter c:\n"))
     discriminant=m.pow(b,2)-4*a*c
     if discriminant>0:
         x1=(-b+m.sqrt(discriminant))/(2*a)
         x2=(-b-m.sqrt(discriminant))/(2*a)
         print("Уравнението има 2 реални корена:")
         print(x1)
         print(x2)
     elif discriminant==0:
         x1=(-b+m.sqrt(discriminant))/(2*a)
         print("Уравнението има един реален корен:")
         print(x1)
     elif discriminant<0:
         print("Уравнението има 2 комплекси корена:")
         x1=(-b+discriminant**0.5)/(2*a)
         x2=(-b-discriminant**0.5)/(2*a)
         print(x1)
         print(x2)

def four():
  print("--4--")
  n=int(input("Enter number:\n"))
  if(n%2==0 and n%3==0 and n%7==0):
      print("Числото се дели успешно")
  else:
      print("Числото не се дели")

def five():
    print("--5--")
    n=int(input("Enter number:"))
    suma=0
    for i in range(1,n+1):
        suma+=i
    print(suma)

def six():
    print("--6--")
    n=int(input("Enter number:"))
    for i in range(1,21):
        print(f"{n}*{i}={n*i}")

def seven():
       print("--7--")
       n=int(input("Enter number:"))
       product=1
       if n>=10:
           for i in range(10,n+1):
               product*=i
           print(product)
       else:
           print("invalid number!")

def eight():
    print("--8--")
    start=int(input("Enter start:"))
    end=int(input("Enter end:"))
    suma=0
    if start!=end:
        for i in range(start,end+1):
            if i%2==0:
                suma+=i
        print(suma)
    else:
        print("Numbers must not be equal!")

def nine():
    print("--9--")
    start=int(input("Enter start:"))
    end=int(input("Enter end:"))
    product=1
    if start!=end:
        for i in range(start,end+1):
            if i%2!=0:
                product*=i
        print(product)
    else:
        print("Numbers must not be equal!")

def ten():
      print("--10--")
      n=int(input("Enter number:"))
      count=0
      for i in range(1,n+1):
          if i%3==0:
              count+=1
      print(count)

def eleven():
      print("--11--")
      n=int(input("Enter number:"))
      suma=0
      for i in range(1,n+1):
            suma+=i**2
      print(suma)

def twelve():
     print("--12--")
     n=int(input("Enter number:"))
     suma=0
     for i in range(1,n+1):
            suma+=(i**2)/i+1
     print(suma)

def thriteen():
     print("--13--")
     n=int(input("Enter number:"))
     suma=0
     for i in range(1,n+1):
            suma+=((i**2)-1)/((i**2)+1)
     print(suma)

def fourteen():
     print("--14--")
     n=int(input("Enter number:"))
     product=1
     for i in range(2,n+1):
            product*=i-1/i+1
     print(product)

def fiveteen():
    print("--15--")
    n=int(input("Enter number:"))
    i=-1
    count=0
    if n<0:
        while i>=n:
            if i%7==0:
                count+=1
            i-=1
        print(count)
    else:
        print("Number must be negative!")

def sixteen():
    print("--16--")
    n=int(input("Enter number:"))
    i=0
    while i<=n:
        if i**2<n:
            print(i)
        i+=1

def seventeen():
    print("--17--")
    n=int(input("Enter number:"))
    for i in range(0,n):
        curNum=i
        nextNum=i+1
        if curNum+nextNum<=n:
            print(curNum)

def eighteen():
     print("--18--")
     n=int(input("Enter number:"))
     print("*")
     for i in range(2,n):
         print("*"+(i-2)*" "+"*")
     print(n*"*")

def nineteen():
    print("--19--")
    n=int(input("Enter number:"))
    print(n*"*")
    for i in range(2,n):
        print("*"+(n-2)*" "+"*")
    print(n*"*")

print("statements")
one()
two()
three()
four()
print("loops")
five()
six()
seven()
eight()
nine()
ten()
eleven()
twelve()
thriteen()
fourteen()
fiveteen()
sixteen()
seventeen()
eighteen()
nineteen()