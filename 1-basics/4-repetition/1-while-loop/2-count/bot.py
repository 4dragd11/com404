#Display the message and ask question to user
print ("How many live cables should I avoid?")
live_cables = int(input())

#Control variable
avoided_cables = 0

while (avoided_cables < live_cables) :
    print ("Avoiding...")

#Update control variable and display final message to user
    avoided_cables = avoided_cables + 1
    print ("Done!", avoided_cables, "live cables avoided.")

print ("\n All live cables have been avoided.")
