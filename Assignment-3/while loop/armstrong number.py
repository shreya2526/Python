num= int(input("enter a three digit number: "))
sum=0
temp=num
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
if (num==sum):
    print(num,"number is an armstrong number")
else:
    print(num,"number is not an armstrong number")
