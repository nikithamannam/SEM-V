def fun():
    a,b,c,d,e = 1,2,3,4,5
    str = "Aditya Chandra"

print("Total local variables: ", fun.__code__.co_nlocals)

def count_local_variables():
    # Define some local variables
    var1 = 10
    var2 = "hello"
    var3 = [1, 2, 3]

    # Get the dictionary of local variables
    local_vars = locals()

    # Count the number of local variables
    num_local_vars = len(local_vars)

    return num_local_vars

result = count_local_variables()
print("Number of local variables:", result)

