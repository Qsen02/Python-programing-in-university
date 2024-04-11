def one():
    print("--1--")
    list1=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        if n.isnumeric():
            list1.append(n)
    print(list1)
    print(len(list1))
def two():
    print("--2--")
    symbol=input("Enter symbol:")
    list2=["a","b","a","a","b","c","b","c","h","d","e","j","k","j"]
    print(list2.count(symbol))
def three():
    print("--3--")
    even=[]
    odd=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        if n.isalpha():
            continue
        n=int(n)
        if n%2==0:
           even.append(n)
        else:
            odd.append(n)
    print(f"odd numbers:{odd}")
    print(len(odd))
    print(f"even numbers:{even}")
    print(len(even))
def four():
    print("--4--")
    list1=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        if n.isalpha():
            continue
        n=int(n)
        list1.append(n)
    print(sum(list1)/len(list1))
def five():
    print("--5--")
    list1=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        n=int(n)
        list1.append(n)
    list2=list1[::2]
    list2.reverse()
    print(list2)
def six():
    print("--6--")
    list1=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        n=int(n)
        list1.append(n)
    print(sum([int(x)**2 for x in list1]))
def seven():
    print("--7--")
    list1=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        n=int(n)
        list1.append(n)
    limit=int(input("Enter limit:"))
    buf=""
    for i in range(0,limit):
        curNum=list1[i]
        nextNum=list1[i+1]
        if curNum+nextNum<=limit:
           curNum=str(curNum)
           buf=curNum+" "
    print(buf)
def eight():
    print("--8--")
    list1=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        list1.append(n)
    start=int(input("Enter start:"))
    end=int(input("Enter end:"))
    print(list1[start:end])
def nine():
    print("--9--")
    list1=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        n=int(n)
        if n<0:
            continue
        list1.append(n)
    list1.reverse()
    print(list1[::])
def ten():
    print("--10--")
    list1=[]
    while True:
        n=input("Enter next:")
        if n=="s":
            break
        n=int(n)
        list1.append(n)
    print(sum([x for x in list1 if x%2==0]))
    product=1
    for element in list1:
        if element%2!=0:
            product*=element
    print(product)
def eleven():
    print("--11--")
    list1=[]
    end=False
    while True:
        row=[]
        for i in range(3):
           n=input("Enter next:")
           if n=="s":
             end=True
             break
           row.append(n)
        if len(row)>0:
           list1.append(row)
        print()
        if end:
            break
    for element in list1:
        print(element[::])
def twelve():
    print("--12--")
    list1=[]
    end=False
    while True:
        row=[]
        for i in range(len(list1)+1):
           n=input("Enter next:")
           if n=="s":
             end=True
             break
           row.append(n)
        if len(row)>0:
           list1.append(row)
        print()
        if end:
            break
    for element in list1:
        print(element[::])
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
eleven()
twelve()