l=[]
def toCelsius(temp):
        a=str(temp)+"F"
        newtemp= (temp-32)*9/5
        print("The temperate is: ",newtemp,"C")
        b=str(newtemp)+"C"
        l.append(newtemp)
def toFahren(temp):
        a=str(temp)+"C"
        newtemp=(temp+32)*(5/9)
        print("The temperate is: ",newtemp,"F")
        b=str(newtemp)+"F"
        l.append((a,b))
def history(l):
        for i in range(0,len(l)):
            #f=l[i]
            #g=l[i+1]
            #z = list(zip(f,g))
            #print(z)
            print("["+ l[i-1]+"->"+l[i]+ "]\n")
while True:
    n=int(input("Enter your choice\n 1:Convert from  Fahrenheit to Celsius \n 2:Convert from Celcius to Fahrenheit\n 3:View History\n"))
    if n == 1:
        temp=int(input("Enter the temperate in Fahrenheit"))
        toCelsius(temp)
    elif n==2:
        temp = int(input("Enter the temperate in Celsius"))
        toFahren(temp)
    elif n==3:
        history(list)
    else:
        print("Invaid input")
