a={}
n=int(input('enter no of items: '))
for i in range(n):
    k=input("enter keys: ")
    v=input("enter values: ")
    a.update({k:v})
print(a)
Key=input("enter key to add: ")
value=input('enter value to add: ')
a.update({Key:value})
print(a)