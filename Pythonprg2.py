students = {'1MS17IS148': 'Asha', '1MS17IS132': 'Ashok', '1MS17IS223' : 'Musaddi lal'}
list1= ["value1", "value2", "value3", "value4"]
list2 = []
j=0;
#print the students name
for i in students:
        #Equal indentation implies that block is in for loop
	print("Key is ", i , "value is ", students[i])
	list1[j] = students[i]
	#list2[j] = i
	j=j+1

print(list1)
print(students.keys())
print(students.values())
print (students.items())
