list=[]
tuple=()
def toCelsius(temp):
        list.append(temp)
        newtemp= (temp-32)*9/5
        print("The temperate is: ",newtemp,"C")
        list.append(newtemp)
def toFahren(temp):
        list.append(temp)
        newtemp=(temp+32)*(5/9)
        print("The temperate is: ",newtemp,"F")
        list.append(newtemp)

n=int(input("Enter your choice\n 1:Convert from  Fahrenheit to Celsius \n 2:Convert from Fahrenheit to Celcius\n"))
for x in range(0, 100):
    if n == 1:
        temp=int(input("Enter the temperate in Fahrenheit"))
        toCelsius(temp)
    elif n==2:
        temp = int(input("Enter the temperate in Celsius"))
        toFahren(temp)
    else:
     print("Invaid input")



