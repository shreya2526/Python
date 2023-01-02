n = int(input("Enter length of list: "))
lst=[]
for n in range(n):
    numbers = int(input('Enter number '))
    lst.append(numbers)
avg=sum(lst)/len(lst)
print("Sum and average of elements in given list is :", sum(lst)," & ", avg)

