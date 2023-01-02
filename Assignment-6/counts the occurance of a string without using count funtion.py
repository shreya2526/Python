text=input("enter a string: ")
ch=input("enter character to be searched: ")
count=0;
for c in text:
    if ch==c:
        count+=1
print(f"{ch} occurs {count} times")