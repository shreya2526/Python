a= input("Enter something: ")
if(a.isnumeric()):
    print("it is an integer value")
elif(a.isalpha()):
    if(a.islower()):
        print("alphabet is in lower csae")
    else:
        print("alphabet is in upper case")
else:
    print("Invalid syntax")