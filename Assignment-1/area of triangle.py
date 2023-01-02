a= float(input("enter the 1st side of triangle: "))
b= float(input("enter the 2nd side of triangle: "))
c= float(input("enter the 3rd side of triangle: "))
print(a,b,c)
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area= ",area)