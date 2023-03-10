user = input("Enter the words : ")
l = 0
u = 0

for i in user:
    if(i>='a' and i<='z'):
        l += 1

    if(i>='A' and i<='Z'):
        u += 1

print("Number of lowercase characters : ", l)
print("Number of uppercase characters : ", u)  