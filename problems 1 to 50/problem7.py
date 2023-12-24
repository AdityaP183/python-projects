# Calculate the sum of all elements in a list.
user_list = []

list_size = int(input("Enter the size of the list: "))

for i in range(list_size):
    item = int(input(f"Enter the item at index {i + 1}: "))
    user_list.append(item)

list_total = 0
for i in range(len(user_list)):
    list_total += user_list[i]

print("Total of all elements in list: ", list_total)