def OddRange(num1,num2):
    arr=[]
    for x in range(num1,num2):
        if x%2!=0:
            arr.append(x)
    return(arr)
num1,num2=map(int,input("Enter the numbers ").split(' '))
arr=OddRange(num1,num2)
print(arr)
