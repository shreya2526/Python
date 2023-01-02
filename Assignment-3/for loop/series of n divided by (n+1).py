num = int(input("enter the number: "))
i=1
sum=0
for i in range(1,num+1):
    series = i/(i+1)
    sum+=series
print("sum of the series is: ",sum)