#dictionary (no index is ordered)
dict = {
    "Name" : "Shubham Kumar",           
    "Age" : 18,
    "DOB" : "18-Jan-2008",
    "List" : ["List", "BHi", "Add", "kar", "skte", "hai"],
    "tupple" : ("tuple", "BHi", "Add", "kar", "skte", "hai")
}
print(dict)
print(dict["Name"])
print(dict["tuple"])                   #value access krne ke liye index nhi hota key use krni hai
dict["Age"] = "17"
dict["Name"] = "Awasthi"
dict["addition of key value pair"] = "added"
print(dict)



#null dict
null_dict = {}
print(null_dict)
print(type(null_dict))
null_dict["Name"] = "Shubham"
print(null_dict)



#nested dict
student = {
    "name" : "shubham",
    "subjects" : {
        "maths" : 91,
        "physics" : 89,
        "chemistry" : 80
    },
    "Roll no" : "28125132"
}
print(student)
print(student["subjects"])
print(student["subjects"]["maths"])






#special uses
student = {
    "name" : "shubham",
    "subjects" : {
        "maths" : 91,
        "physics" : 89,
        "chemistry" : 80
    },
    "Roll no" : "28125132"
}
print(student.keys())
print(list(student.keys()))
print(tuple(student.keys()))
print(len(student.keys()))
print(len(list(student.keys())))

#     #values ke sath bhi same kr skte hai 
print(student.values())
pairs = list(student.values())
print(pairs[0])

    #values lene ke ways
print(student["subjects"])   #-->error on mistakes
print(student.get("subjects"))    #-->none on mistake or no key available
print(student.get("subjects2"))


    #update dict
student.update({"age" : "18"})    #-->for single update
print(student)
  #or
new_dict = {"rehne de" : "ok"}    #--> for multiple updates
student.update(new_dict)
print(student)


#setssss
a = {1,2,3,4,5,6,7,8,9,0}
print(a.pop())
print(a.pop())
print(a.add(11))
print(a)
a.remove(3)
print(a)
a.clear()
print(a)

#union and intersection
a = {1,2,3,4}
b = {3,4,5,6}
print(b.union(a))
print(a.intersection(b))
print(b)



#practice problems
#storing words     (1)
dic = {
    "table" : ["a", "b"],
    "cat" : "A small animal"
}
print(dic)


#practise question 2 
#a list of subjects is given find no of classromm req for students if one sub takes one class
#unique values ka count chahiye to set me store krke lenght nikalo...





#marks store krne hai dict me
a = {}
maths_marks = int(input("Marks in maths?"))
a.update({"Maths" : maths_marks})
physics_marks = int(input("Marks in physics?"))
a.update({"Physics" : physics_marks})
chem_marks = int(input("Marks in chemistry?"))
a.update({"Chemistry" : chem_marks})
print(a)



#figure out way to store 9 and 9.0 as diff values in sets
a = {9,"9.0",9.0}
print(len(a))
print(a)
