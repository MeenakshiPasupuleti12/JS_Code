num = int(input("Enter a number: "))  # Taking integer input

# Loop to process a range of numbers
for i in range(num):  
    value = input("Enter a value: ").split()  # Taking space-separated input and splitting it into a list
    print("You entered:", value)  # Displaying the input values
