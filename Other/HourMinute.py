def hourMinute(num):
    a=int(num)//60
    b=int(num)%60
    c=str(a)+":"+str(b)
    print(c)
num=input("Enter the number")
hourMinute(num)
