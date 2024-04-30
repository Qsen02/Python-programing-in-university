def one():
    try:
        f=open("string_data.txt","r")
        strings=f.read().split("\n")
        strings.reverse()
        newString="\n".join(strings)
        nf=open("string_reverse.txt","a")
        nf.write(newString)
    except:
        print("File is not found!")
def two():
    try:
        f=open("int_data.txt ","r")
        mylist=f.read().split(",")
        listOfNumbers=[]
        for el in mylist:
            curEl=int(el)
            strEl=str(curEl*2)
            listOfNumbers.append(strEl)
        stringOfNumbers=", ".join(listOfNumbers)
        nf=open("doubled_ints.txt","a")
        nf.write(stringOfNumbers)
    except:
        print("file is not found!")
def three():
    try:
        f=open("mixed_data.txt ","r")
        studentList=f.read()
        newList=studentList.split("\n")
        for typel in newList:
            number=typel.split(", ")[0]
            name=typel.split(", ")[1]
            nf=open("numbers.txt","a")
            nf.write(number+", ")
            sf=open("names.txt","a")
            sf.write(name+", ")
    except:
        print("File is not found!")
def four():
    try:
        f=open("math_data.csv","r")
        x=[]
        y=[]
        coordList=f.read().split("\n")
        coordX=coordList[0].split(", ")
        coordY=coordList[1].split(", ")
        for coord in coordX:
            curCoord=int(coord)
            x.append(curCoord)
        for coord in coordY:
            curCoord=int(coord)
            y.append(curCoord)
        print(x)
        print(y)
    except:
        print("File is not found")
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(x,y)
    plt.show()
def five():
    try:
        import os
        file=open("filenames.txt","r")
        listOfFiles=file.readlines()
        if not os.path.exists("install"):
            os.mkdir("install")
        os.chdir("install")
        for f in listOfFiles:
            file=f.replace("\n","")+".txt"
            nf=open(file,"x")
            nf.close()
            nf=open(file,"w")
            nf.write("work!")
            print(os.path.getsize(file))
            nf.close()
    except:
        print("file or folder is not found!")
one()
two()
three()
four()
five()