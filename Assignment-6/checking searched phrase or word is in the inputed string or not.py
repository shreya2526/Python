str=input("Enter a string: ")
ch=input("The word or phrase you want to search: ")
if ch in str:
    print(ch,"found")
else:
    print("not found")