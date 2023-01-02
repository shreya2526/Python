from curses.ascii import isdigit


text=input("Enter a string with integer number: ")
one_ch = False
one_num=False
for ch in text: 
    if ch.isdigit():
        one_num=True
    if ch.isalpha():
        one_ch=True
if one_num and one_ch:
    print("Input has atleast one number and one word")
else:
    if one_ch:
        print("Input has one word")
    else:
        print("Input has one number")
   