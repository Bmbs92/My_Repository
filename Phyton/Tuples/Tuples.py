#On this script you will find the first guidelines
#to iniciate with Python

#create a tuple
the_tuple=(1,2,3,4,5)
print(the_tuple)
"Tuple can not be modified"

#Access tuples
print(the_tuple[2])
print(the_tuple[2:4])

#count a specific value in a tuple
print("Enter value a value")
value=input()
count_tuple=the_tuple.count(int(value))
print(f"{count_tuple} value found")

#joining tuples
the_tuple_2=(6,7,8)
print(the_tuple+the_tuple_2)