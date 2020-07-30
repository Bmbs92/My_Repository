#If with varibles
a=30
b=38
c=15

##If...else
if(a==b):
    print("They are equal")
else:
    print("They are not equal")

##If...elif...else
if(a>b):
    print("a is not the lowest number")
elif(a>c):
    print("a is not the lowest number")
else:
    print("a is the lowest number")

##Same example but with logical operations
if(a>b) or (a>c):
    print("a is not the lowest number")
else:
    print("a is the lowest number")

#If with a list
my_list=['apples','bananas','grapes']

##If...else
if 'apples' in my_list:
    print("Apples are on the list")
else:
    print("Apples are not on the list")

##If...elif...else
if 'Figs' in my_list:
    print("The fruit is on the list")
elif 'Melons' in my_list:
    print("The fruit is on the list")
else:
    print("The fruits are not on the list")

##Same example but with logical operations
if('apples' in my_list) or ('Berries' in my_list):
    print("At least one fruit is on the list")
else:
    print("Non of the fruits is on the list")

