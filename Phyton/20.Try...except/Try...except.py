
# The loops will try to complete the try statement, if the statement give an error, then the except statement will be executed.
x=10

while x>-5:
    try:
        a=10/x 
        x=x-1  #as the x is reduce, it will be equal to cero in one point      
        print(a)
    except:        
        print("There is exception. Numbers divided by {} result in error".format(x)) #x = 0, numbers divided by cero result in an error
        x=x-1

x=10
while x>-5:
    try:
        a=10/x 
        print(a)
    except:        
        print("There is exception. Numbers divided by {} result in error".format(x)) #x = 0, numbers divided by cero result in an error
    finally: #either the statement is an error or not, do the finally statement
        x=x-1
        print("End of the loop")