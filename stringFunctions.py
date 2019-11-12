def ChangeString(str1):
    for x in str1:
        if x.isalpha():
            a=ord(x)
            b=a+1
            if a==90:
                b=97
            str1=str1.replace(x,chr(b))
    for x in str1:
        if(x=='a' or x=='e' or x=='i'or x=='u' or x=='A'or x=='E' or x=='I' or x=='O' or x=='U'):
            x3=x.upper()
            str1=str1.replace(x,x3)
    print("The new string is: \t",str1)
str1=input("Enter the string")
ChangeString(str1)
