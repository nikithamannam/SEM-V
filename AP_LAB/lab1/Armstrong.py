n= input("enter number")


x=len(n)
armstrong=0

for digit in n:
    armstrong=armstrong+int(digit)**x

   
if armstrong ==int (n):
    print("is an armstrong number")
else:
    print("not an armstrong number")
