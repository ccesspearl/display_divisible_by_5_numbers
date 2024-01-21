# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Pseudocode 

# Create a variable for given list 
given_list = [5,10,15,18,20,24,25]

# Create print messages outside the loop 
print("Given list is", given_list)
print("Divisible by 5:")

# Use for loop 
for i in given_list:
    
# Use if statement and print the results
    if i % 5 == 0: 
        print(i)