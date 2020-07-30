
#Create a function
def hi(): #set up a function with constructor key word def 
    print("hi")
hi() #reproduce the function 

#Add parameters
def sum_values(a,b,c): #parameters a,b,c
    x=a+b+c
    print(x)
sum_values(3,2,6)

#Return function outcome
def diff_value(a,b):
    x=a-b
    return x #return the outcome x
y=diff_value(4,6)
print(y)

#Nested function
def div2(k,z,u): #function 1
    a=diff_value(z,u) #function 2
    x=a/k
    return x
c=div2(2,8,4)
print(c)


