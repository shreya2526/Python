n = int(input("enter the number until you want to get average: "))
sum=0
i=1
for i in range(i, n+1):
    sum=sum+i
    i=i+1
avg=float(sum/n)
print("the average is: ",avg)