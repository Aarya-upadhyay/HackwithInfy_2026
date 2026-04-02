def gradingStudents(grades):
    for i in range(len(grades)):
        # Rule: Only round if grade is 38 or higher
        if grades[i] >= 38:
            # Find how much we need to reach the next multiple of 5
            # Example: 73 % 5 is 3. Next multiple is 73 + (5 - 3) = 75.
            remainder = grades[i] % 5
            
            if remainder >= 3: # This means the difference is less than 3
                grades[i] += (5 - remainder)
                
    return grades # Move this OUTSIDE the for loop
