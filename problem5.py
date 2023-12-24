# Find the largest element in a list.
user_list = []

list_size = int(input("Enter the size of the list: "))

for i in range(list_size):
    item = int(input(f"Enter the item at index {i + 1}: "))
    user_list.append(item)

user_list.sort(reverse=True)
print("The largest element in the list:", user_list[0])