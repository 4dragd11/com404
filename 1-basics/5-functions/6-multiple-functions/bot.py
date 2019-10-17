def display_ladder (steps):
    steps_ladder = 0
    while (steps_ladder < steps):
        steps_ladder = steps_ladder + 1
        print ("\n | |")
        print ("\n ***")
    print("\n | |") 
    

        
def create_ladder ():
    print("How many steps remain?")
    steps_remain = int(input())
    display_ladder(steps_remain)

create_ladder ()
