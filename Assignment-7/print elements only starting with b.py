lst=input("enter elements: ")
user_lst=lst.split()
for val in user_lst:
    if 'b' in val:
        print(val,end=" ")