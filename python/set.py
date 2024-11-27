#dictionary inpython
#dictionaries are used to store data values in key:value pairs
#they are unordered,mutable (changeable)& don't allow duplicate keys
#dict={
 #   "name":"Ritu",
  #  "learning" : "coding",
   # "age": 22,
    #"is_adult": True,
    #"marks": 88.8
#}
#print(type(dict)) 
#print(dict['name'])
#print(dict['age'])
#print(dict['marks'])
#null_dict={}
#null_dict["name"]="Ritu"
#print(null_dict)

#nested dictionaries
student={
    "name":"RITU BHARTI",
    "subject":{
               "op":89,
               "dsa":90,
               "c++":67,
               "python":89,
               "java":77}
    
}
new_dict={}
student.update({"city":"delhi"})
print(student)
print(student["subject"]["dsa"])
#print(list(student.keys()))
#print(len(student))
#print(list(student.values()))
#print(student.items())
print(student["name"])
print(student.get("name"))
print(student.update())

#set is the collection of the unordered items.
#each element in the set must be unique & immutable.
collection={1,2,3,4,"hello","world","world"}
print(collection)
print(len(collection))
#types= set()
#print(type(types))
collection.add(5)
collection.remove("hello")
print(collection.pop())
set1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2))#{2,3}
print(set1)
print(set2)

#store following word meaning in a python dictionary:
dict={"cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]
 }
print(dict)
print(type(dict))

#you are given a list of subject for students.
#aasume one classroom is required for 1subject.how many classroom are needed by all students.
subject={"python","java","c++",
         "python","javascript","java",
          "python","java","c++","c"}
print(subject)
print(len(subject))

#WAP to enter marks of 3 subject from the user and store them in a dicitionary .
#start with an empty dicitonary & add one by one
#use subjet name as key & marks as value.
marks={}
x=input("enter op:")
marks.update({"op":x})
x=input("enter c++:")
marks.update({"c++":x})
X=input("enter python:")
marks.update({"python":x})
print(marks)

