def ChangeString(str1):
    str2=""
    for x in str1:
        if x.isalpha():
            x2=ord(x)
            x2=x2+1
            #str2+=chr(x2)
            str1=str1.replace(x,chr(x2))
            x2=0
    for x in str1:
        if(x=="a"or x=="e" or x=="i" or x=="o" or x=="u"):
            x3=x.upper()
            str1=str1.replace(x,x3)
    print("The new string is:\t",str1)

str1=input("Enter the string")
ChangeString(str1)
