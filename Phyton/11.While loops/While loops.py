
#Add one until x=9
x=1
while x<10:
    print(x)
    x=x+1

#Add one until y <10 and break the loop until y <4
y=1
while y<10:
    if(y==4):
        break #if y=4 break the loop
    else:
        print(y)
        y=y+1

#Double while
a=2
b=3
while a<10:
    a=a+1
    while b<8:
        b=b+1
        print("{} plus {} equals {}".format(a,b,a+b))