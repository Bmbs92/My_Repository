#On this script you will find the first guidelines
#to iniciate with Python

#string literals

#slicing, character position
a="your name"
print(a[3])
"print = r"
print(a[0:4])
"print=your"
print(a[-10:-5])
"print=your"

#len
print("Enter your name")
name=input()
len_name=len(name)
print(len_name)

#replace
text="Hi name, how are you?"
print(text.replace("name",name))

#lower & upper
a= " HeLlo you"
print(a.lower())
print(a.upper())

#Check string
a="Hello you"
verify_1= "ello" in a
verify_2="ello" not in a
print(verify_1)
print(verify_2)

#String format
print("Enter your lastname")
last_name=input()
text="Hello {} {}"
print(text.format(name,last_name))

#find & index
print("Enter the value you want to find")
value=input()
a=name.find(value)
b=name.index(value)
print(a)
print(b)
