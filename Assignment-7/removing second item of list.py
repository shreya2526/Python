input_list=input("enter elements using space: ")
user_list=input_list.split()
print("list: ",user_list)
del user_list[1]
print("Current list: ",user_list)