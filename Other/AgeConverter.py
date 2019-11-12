from datetime import date
def AgeConverter(date2):
    date1=date.today()
    age=date1.year-date2.year
    return(age)
print("Enter date in yyyy-mm-dd")
year=int(input())
month=int(input())
daten=int(input())
date2=date(year,month,daten)
age=AgeConverter(date2)
print("The age is: \t",age)
