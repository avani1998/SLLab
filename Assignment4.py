#10-10

#3 Return hours and minutes

def HourMinute(num1):
        a=num1//60
        b=num1%60
        c=str(a)+":"+str(b)
        return (c)

num1=int(input("Enter the number\n"))
sum=HourMinute(num1)
print("The hours and minutes are :",sum)

#4
from datetime import date
def AgeConvert(date2):
    date1=date.today()
    return (date1.year-date2.year)

print("Enter date in dd-mm-yyyy")
year=int(input())
month=int(input())
datev=int(input())
date2=date(year,month,datev)
age= AgeConvert(date2)
print(age)

#5
def OddRange(num1,num2):
    list1=[]
    for x in range(num1,num2):
        if x%2!=0:
            list1.append(x)
    return(list1)

a=int(input("Enter the starting number"))
b=int(input("Enter the ending number"))
print(OddRange(a,b))
