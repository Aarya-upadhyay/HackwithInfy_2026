def truckTour(petrolpumps):
    tank = 0
    start = 0
    
    # Iterate through all pumps using the correct variable name
    for i in range(len(petrolpumps)):
        # Unpack the petrol available and distance to the next pump
        p, d = petrolpumps[i]
        
        # Add available petrol and subtract distance to get current surplus
        tank += p - d
        
        # If tank goes negative, this start point (and all points before it) 
        # cannot be the starting pump.
        if tank < 0:
            start = i + 1
            tank = 0
            
    return start
