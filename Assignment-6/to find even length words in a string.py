text=input("Enter a string: ")
mylist=text.split(" ")
for word in mylist:
    if (len(word)%2==0):
        print(word)