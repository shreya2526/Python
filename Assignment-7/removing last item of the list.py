input_list=input("enter elements using space: ")
user_list=input_list.split()
print("list: ",user_list)
user_list.pop()
#del user_list[-1]
print("removed the last item: ",user_list)