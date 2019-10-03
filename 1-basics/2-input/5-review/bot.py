# Ask user for eye character 
print("Please enter an eye character:")
eye = input() 

# Ask user for the length of the glasses
print("Please enter the length of the glasses:")
length = int(input())

# Display an ascii glasses
print()

print("#########" + (" " * length)  + "#########")
print("#   " + eye + "   #" + ("#" * length) + "#   " + eye + "   #")
print("#########" + (" " * length) + "#########")

print()