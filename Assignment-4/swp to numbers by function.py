def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print('\nAfter swapping x=',a,'y=',b)
x=int(input('enter 1st number: '))
y=int(input('enter 2nd number: '))
print('before swapping: ')
print(x,y,end=' ')
swap(x,y)
