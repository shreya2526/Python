a= int(input("enter 1st number: "))
b= int(input("enter 2nd number: "))
c= int(input("enter 3nd number: "))
D=(b**2 - 4*a*c)
if(D>=0):
    root1= (b+D**0.5)/2*a
    root2= (b-D**0.5)/2*a
    print(root1, root2, sep="\t")
else:
    print("roots are imaginary")


