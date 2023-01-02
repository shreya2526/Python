num= int(input("enter a number: "))
rev_num=0
while(num>0):
    remainder = num%10
    rev_num= (rev_num*10)+remainder
    num=num//10
print("the reversed num of is: {}".format(rev_num))