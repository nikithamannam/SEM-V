def get_unique_elements(input_list):
    unique_elements = list(set(input_list))
    return unique_elements

# Taking input from the user
input_list = input("Enter a list of elements separated by spaces: ").split()

# Calling the function to get unique elements
unique_elements = get_unique_elements(input_list)

print("Unique elements:", unique_elements)
