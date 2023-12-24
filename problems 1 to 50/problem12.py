# Find the common elements between two lists.
user_list1 = []
user_list2 = []

list_size = int(input("Enter the size of the list: "))

for i in range(list_size):
    item = int(input(f"Enter the item for first list at index {i + 1}: "))
    user_list1.append(item)

for i in range(list_size):
    item = int(input(f"Enter the item for second list at index {i + 1}: "))
    user_list2.append(item)

common_elements = [common for common in user_list1 if common in user_list2]
print(common_elements)