def factorial(n):
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i
    return fact
n=int(input('enter the value of n: '))
sum=0
for i in range(1,n+1,1):
    series =(i**i)/factorial(i)
    sum=sum+series
print('sum of the series is: ',sum)