# Write a Python program to check if a number is prime.
def is_prime(number):
    if(number > 1):
        for i in range(2, int(number/2)+1):
            if(number % i == 0):
                return False    
        return True
    elif(number == 2): 
        return True
    else:
        return False
    
num = int(input("Enter the number to check if it's prime: "))
if(is_prime(num)):
    print("Number is prime")
else:
    print("Number is not prime")