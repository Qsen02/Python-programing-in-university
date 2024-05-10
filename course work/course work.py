# Импортваме необходимите библеотеки
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,lambdify
import random

# Потребителя избира каква ще е буквата на променливата с която ще се работи в уравнението
symbol=input("Enter letter for variable in equation:\n")
# Лист с различни цветове за чертаене
listcolors=["blue","red","green","purple","pink","brown","black","yellow","orange"]
# Тук потребителя въвжеда уравнението
equation=input("Enter equation with this variable:\n")
# Въведеното от потребителя уравнение го превръщаме във функция в python
x=symbols(symbol)
function=lambdify(x,equation)
# Тук посочваме интервала в който да бъде изчертана функцията и броя точки които са на равно разстояние в графиката
x = np.linspace(-15, 15,200)
# След това за всяка точка прилагаме функцията която сме създали
y = function(x)
# Тук разбъркваме листа с цветовете и взимаме първия елемент , за да може при всяко чертаене да виждаме различен цвят
random.shuffle(listcolors)
index=random.randint(0,8)
# Тук вече изчертаваме графиката
plt.plot(x, y,c=listcolors[index])
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Графика на функцията: {equation}")
plt.grid(True)
plt.show()
