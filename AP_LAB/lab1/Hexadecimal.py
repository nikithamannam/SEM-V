s=input("enter a number:")

for char in s :
    if (char>='0' and char<='9')or (char>='A'and char<='F'):
        continue
    else:
        print ("not a hexadecimal")
        break
else:
    print ("is a hexadecimal")
