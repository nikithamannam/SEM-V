def print_pascals_triangle(n):
    if n <= 0:
        return
    
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
    
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print(binomial_coefficient(i, j), end=" ")
        print()

# Call the function with the desired number of rows
num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
print_pascals_triangle(num_rows)
