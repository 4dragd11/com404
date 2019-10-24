# Loop
print ("How many miles must I travel before I reach the secret base?")
number = int(input())
print ("I will count the miles...")
print ("\n")

miles = number

while (miles > 0):
    print("I have", miles, "miles to go before I reach the base.")
    miles = miles - 1

