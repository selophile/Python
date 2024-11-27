#A bulit-in data type that stores set of values
#it can store elements of different types(integer ,float, string,etc.)
#marks=[94.4,87.5,95.2,66.4,45.1]
#print(marks)
#print(type(marks))
#rint(marks[1])
#print(len(marks))

#student=["Ritu",89.9,88,"patna"]
#print(type(student))
#print(len(student))
#print(student[2])

#marks=[94.4,87.5,95.2,66.4,45.1]
#list1=[2,1,3]
#print(list1)
#print(marks[-3:-2])
#list1.append(4)
#print(list1)
#list1.sort()
#print(list1)
#list1.reverse()
#print(list1)
#list1.insert(0,2)
#print(list1)
#list1.sort(reverse=True)
#print(list1)
#list1.pop(2)
#print(list1)
#list1.remove(1)
#print(list1)

#tuple 
#a bulit -in data type that lets us create immutable sequences of values.
#tup=(89,87,64,33,99)
#print(tup)
#print(tup[1])
#print(type(tup))
#print(len(tup))
#tup=(1,2,3,4)
#print(tup)
#print(tup.index(1))
#print(tup.count(1))

#WAP to ask the user to enter names of their 3 movies & store them in a list
#movies=[]
#mov1=input("enter 1st movies:")
#movies.append(mov1)
#mov2=input("enter 2nd movies:")
#movies.append(mov2)
#mov3=input("enter 3rd movies:")
#movies.append(mov3)
 
#print(movies)

#WAP  to check if a list contains a palindrome of element .(hint:use copy()method)
#[1,2,3,2,1][1,"abc","abc",1]
#list1=[1,2,1]
#list2=[1,2,3]
#copy_list1=list1.copy()
#copy_list1.reverse()
#if(copy_list1==list1):
 #   print("palindrome")
#else:
 #  print("NOT palindrome")    

#WAP to count the number of students with the"A" grade in the following tuple.

Grade=["C","D","A","A","B","B","A"]
print(Grade.count("A"))

#store the above values in a list $ sort them from "A" to "D".
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)