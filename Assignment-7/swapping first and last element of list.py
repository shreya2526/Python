n=int(input("Enter the no of list element: "))
input_list=input("Enter the elements: ")
user_list=input_list.split()
print("Inputed list: ",user_list)
temp=user_list[0]
user_list[0]=user_list[n-1]
user_list[n-1]=temp
print(user_list)
print("List after swapping: ",user_list)