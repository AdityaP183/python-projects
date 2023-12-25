# 15. Write a program to generate Fibonacci series.
limit = int(input("Enter the limit to generate Fibonacci series: "))
list_of_fibonacci = [0, 1]

while list_of_fibonacci[-1] + list_of_fibonacci[-2] <= limit:
    num = list_of_fibonacci[-1] + list_of_fibonacci[-2]
    list_of_fibonacci.append(num)

print(f"Fibonacci series till {limit}: {list_of_fibonacci}")