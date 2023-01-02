import operator
input_list=input("Enter the elements: ")
user_list=input_list.split()
ch=input("Enter the element you want to find: ")
count=operator.countOf(user_list,ch)
print(ch," has occured ",count," times in the list")