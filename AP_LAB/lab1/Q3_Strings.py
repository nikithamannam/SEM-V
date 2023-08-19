
input_string = input("Enter N Strings: (Separated by \', \')\n")

l1 = input_string.split(", ")

odd_length = []
first_last_same = []

for s in l1:
    if len(s) >= 2:
        if s[0] == s[-1]:
            first_last_same.append(s)
    if len(s)%2 == 1:
        odd_length.append(s)

print("Number of strings with same first and last characters : " , len(first_last_same))
print(first_last_same)
print("\nStrings with odd length", odd_length)
