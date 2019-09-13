
newlist=[]
lsit=[]
def inputuser():
    n= int(input("Enter number of elements"))
    newlist = []
    for i in range(0, n):
        ele = int(input("Enter the elements"))

        newlist.append(ele)
    print(newlist)

def remove_duplicattes(numbers):
    newlist = []
    for number in numbers:
        if number not in newlist:
            list.append(number)
    print(list)
    return(list)
inputuser()
remove_duplicattes(newlist)







