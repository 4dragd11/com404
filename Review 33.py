# Loop
print ("How many zones must I cross?")
user_response = int(input())
print ("Crossing zones...")

number = user_response

while (number > 0) :
    print ("…crossed zone", number) 
    number = number - 1  
print ("Crossed all zones.  Jumanji!")      
