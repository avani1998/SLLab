#Q1 
items1 =['cabbage','tomato','cauliflower','broccoli']
print('Length of list is:\n') 
print(len(items1))
print('List as an element of existing list:')
items2 = ['potato','onion']
items1.append(items2)
print('Using Slice Operator')
print("Items 2 to 3 are:" ,items1[2:4])
print("Last 3 items are:" ,items1[:3])
print(items1[:-3])
print(items1[2:])
print(items1[:])
print("\n Replace second element with a fruit name")
items1[1]='apple'
print(items1)
print('\n concatinate two lists')
print(items1 + items2)
print('The coppied list are')
newlist1 = items1.copy()
newlist2 = list(items1)
print(newlist1)
print(newlist2)

#Q2
tuple1 = ('1','2','3','4','5','6','7','8','9','10')
print(tuple1[5])
print(list(tuple1))
