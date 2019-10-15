#Pgm to understand else-if

x = -3 #Have to give this line, else error: "NameError: name x is not defined"
if x > 0.0:
 print("Positive")

elif x < 0.0:
 print("Negative")
 x= -1.0*x

else:
 print("zero")

#Another way

if x > 0.0:
 print("+ve")

else:
 if x < 0.0:
  print("-ve")
  x= -1.0*x

 else:     #Inside outer else
  print("0")
