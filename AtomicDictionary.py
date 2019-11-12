ele={'H':'Hydrogen','He':'Helium','Li':'Lithium','Be':'Berilium','B':'Boron'}
print("Original dictionary\n",ele)
u=input("Enter a unique element")
ele[u]=input("Enter the name")
print("The new dictionary is\n")
print(ele)
d=input("Enter a duplicate element")
ele[d]=input("Enter the name")
print("The updated dictionary is\n",ele)
print("length of dictionay is\t",len(ele))
print("-------Searching-------")
s=input("Enter a symbol to search for\t")
if s in ele:
    print(ele[s])
p=input("Enter the name of element to search for symbol")
if p in list(ele.values()):
    for i in ele:
        if ele[i]==p:
            print(i)
