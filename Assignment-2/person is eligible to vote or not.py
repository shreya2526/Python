age = int(input("enter your age: "))
if(age>=18):
    print("you are eligible to vote")
else:
    c= 18-age
    print("there are",c,"years left to vote")