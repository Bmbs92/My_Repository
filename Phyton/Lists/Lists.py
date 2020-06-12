#On this script you will find the first guidelines
#to iniciate with Python

#create a ist
the_list=[1,2,3,4,5,6]
print(the_list)

#print list
print(the_list[3])
print(the_list[-1])
print(the_list[2:4])

#add values to the list
the_list.append(7)
print(the_list)

#add more than one value
the_list.extend([7,8,"nine"])
print(the_list)

#change value
the_list[9]=9
print(the_list)

#remove values
the_list.remove(7)
print(the_list)

#Index with list
"List does not have find attribute"
a=the_list.index(3)
print(a)

#Len with list
list_len=len(the_list)
print(list_len)