#Create a ist
the_list=[1,2,3,4,5,6]
print(the_list)

#Read list
print(the_list[3])
print(the_list[-1])
print(the_list[2:4])

#Update values
##one value
the_list.append(7)
print(the_list)

##Add more than one value
the_list.extend([7,8,"nine"])
print(the_list)
##Swip value
the_list[9]=9
print(the_list)

##Delete value
the_list.remove(7)
print(the_list)
