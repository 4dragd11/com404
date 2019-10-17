def cross_bridge(steps):
    steps_crossed = 0

    while (steps_crossed < steps):
        steps_crossed = steps_crossed + 1
        print ("Crossed step")

    if (steps <= 5):
        print ("we must keep going!")
    else:
        print ("The bridge is collapsing!")



cross_bridge(5)
cross_bridge(6)