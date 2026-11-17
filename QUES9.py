
n = int(input("How many numbers? "))   
numbers = []                            

for i in range(n):                      
    num = int(input("Enter number: "))  
    numbers.append(num)                 

total = sum(numbers)                    
print("Sum =", total)                 
