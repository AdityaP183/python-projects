# 16. Remove duplicate elements from a list.

user_list = []

list_size = int(input("Enter the size of the list: "))

for i in range(list_size):
    item = int(input(f"Enter the item at index {i + 1}: "))
    user_list.append(item)

new_list = list(set(user_list))

print(new_list)