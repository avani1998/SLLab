list=[]
def inputElements(): 
    n=int(input('Enter number of elemens'))
    for x in range(0,n):
            i=int(input('Enter the elements'))
            list.append(i)
    print(list)
def minandmax():
    print('The minimum is ',min(list))
    print('The maximum is ',max(list))
def insertnew():
    n=int(input('Enter an element to insert'))
    list.append(n)
    print(list)
def delete():
    n=int(input('Enter element to delete'))
    list.remove(n)
    print(list)
def search():
    n=int(input('enter element to search for'))
    if n in list:
        print('Element exist in list')
    else:
        print("Element not in list")
inputElements()
minandmax()
insertnew()
delete()
search()
