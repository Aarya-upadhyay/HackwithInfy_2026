def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse=True)
    j=0
    total_cal=0
    for i in range(len(calorie)):
        total_cal+=(2**j)*calorie[i]
        j+=1
    return total_cal
        
