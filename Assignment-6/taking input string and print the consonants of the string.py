text=input("Enter a string: ")
ans="\0"
vowels="aeiou AEIOU"
for ch in text: 
    if ch not in vowels:
        ans+=ch
print("ithout vowels: ",ans)