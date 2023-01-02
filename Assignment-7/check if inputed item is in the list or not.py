#n=int(input("how many elements you want insert: "))
input_list=input("enter elements using space: ")
user_list=input_list.split()
#print("list: ",user_list)
#print("The second last item of the list is: ",user_list[n-2])
ch=input("enter the element you ant to search: ")
if ch in user_list:
    print(ch,"has been found")    
else:
    print("not found")
    print('main list is: ',user_list)