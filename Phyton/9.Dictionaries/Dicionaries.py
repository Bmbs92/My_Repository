#Create
##Create a dictionary: keys
this_dict={
    "Id": "",
    "Name": "",
    "Age": "",
    "Nationality": ""
}
print(this_dict)

##Create: add values
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

#Read
#Read the value from a key
print(this_dict["Name"])

#Read the value from a key with get()
print(this_dict.get('Name'))

#Read all keys from the dictionary
x=list(this_dict.keys())
print(x)

#Read the first key[0]
x=list(this_dict.keys())[0]
print(x)

#Read all values from the dictionary
x=list(this_dict.values())
print(x)

#Read the first value[0]
x=list(this_dict.values())[0]
print(x)

#Update
#Update values by its key
this_dict["Age"]=28
print(this_dict)

#Update modify the key value
this_dict['Code']=this_dict.pop('Id')
print(this_dict)

#Update by adding new fields
status=input("Enter your status: ")
this_dict["Status"]=status
print(this_dict)

#Delete
#Delete the value
this_dict["Age"]=28
print(this_dict)

#Delete a field
this_dict.pop("Status")
print(this_dict)

