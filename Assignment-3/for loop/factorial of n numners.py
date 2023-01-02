n= int(input("enter the nth number: "))
i=0
fact=1
for i in range(1, n+1):
    fact=fact*i
print("the factorial of",n,"is: ",fact)