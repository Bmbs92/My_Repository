#On this script you will find the first guidelines
#to iniciate with Python

#Create a dictionary
this_dict={
    "Id": "",
    "Name": "",
    "Age": "",
    "Nationality": ""
}
print(this_dict)

#Add values to the dictionary
print("Enter your ID")
input_id=input()
print("Enter your name")
name=input()
print("Enter your age")
age=input()
print("Enter your nationality")
nationality=input()

this_dict["Id"]=input_id
this_dict["Name"]=name
this_dict["Age"]=age
this_dict["Nationality"]=nationality

print(this_dict)

#Access dictionary
print(this_dict["Name"])

#Change values
this_dict["Age"]=28
print(this_dict)

#Adding new fields
print("Enter your status")
status=input()
this_dict["Status"]=status
print(this_dict)

#remove a field
this_dict.pop("Status")
print(this_dict)

