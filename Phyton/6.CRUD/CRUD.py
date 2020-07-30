#Main functions in programming

#C is for create
x='Hi' #create a vairble

#R is for read
print(x) #read the variable

#U is for update
x=x+" you" #update the varible
print(x) 

#D is for delete
x=""
print(x)

#In python there are methods and functions that are use for executing CRUD tasks.

#Step 1: define a varible
your_name=input("Your name: ")

#Step 2: apply CRUD

##Read
###Read values its index
print(your_name[0]) #first value have a index 0
print(your_name[0:2]) # from the index 0 to the index 2
print(your_name[-4:-1]) # negative index = reading from right to left

###Read the index of its value with index method
print(your_name.index('a'))

###Read the index of it value with find method
x=your_name.find('a')
print(x)

###Read value and add format
new_format="Good morning {}, how are you?,".format(your_name)
print(new_format)

##update
###Update with replace
text="Hi name, how are you?"
print(text.replace("name",your_name))

###Update the case
print(your_name.lower())
print(your_name.upper())

