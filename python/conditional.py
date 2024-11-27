
#1 
age=24
if(age>=18):
 print("can vote ")
elif(age==18):
 print("you can vote")
else:
 print("cannot vote")

 
 #2
 light="green"
 if(light=="red"):
  print("stop")
 elif(light=="green"):
  print("go")
 elif(light=="yellow"):
   print("look")
#3
num=3
if(num>2):
 print("greater than 2")
elif(num>3):
  print("greater tha 3")

#Grade students based on marks 

marks=int(input("enter student marks:"))
if(marks>=90):
   garde="A"
elif(marks>=80 and marks< 90):
   garde="B"
elif(marks>=70 and marks<80 ):
   garde="C"
else:
  garde="D"
  print("grade of the student-->",garde)

  #nesting
  age=34
  if(age>=18):
   if(age>=80):
    print("can drive")
   else:
     print("cannot drive")

#WAp to check if a number entered by the user is odd or even
num=(int(input("enter a no.")))

rem=num % 2
print("even")
print("Odd")

 #WAP TO FIND THE greatest of 3 numbers enteredby the user.
a=int(input("enter first  no."))
b=int(input("enter second no."))
c=int(input("enter third no."))
if(a>=b and a>=c):
 print("first no is largest",a)
elif(b>=c):
  print("second no is largest",b)
else:
  print("third is largest",c)

#WAP to check if a number is a multiple of 7 or not
x=int(input("enter number:"))
if(x%7==0):
 print("multipule of 7")
else:
  print("not a multiple")