def fact(n,r):
    f1=1
    f2=1
    for i in range(1,n+1,1):
        f1=f1*i
    for i in range(1,r+1,1):
        f2=f2*i
    value =f1/f2
    print('the value=',value)
n=int(input('enter the value of n='))
r=int(input('enter the value of r='))
fact(n,r)
