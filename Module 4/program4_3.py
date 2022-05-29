# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 4 Assignment
# Collaborators: Kevin Peters, Mohith Prasad, Anas Kimia, Sean Fowler, & Ryan Merritt 

# program4_3.py
# Program Description: Given a sample output, recreate that same output by using nested loops. 

# Start program.
    # For a number (variable 'num') in a range beginning at nine, ending at zero, and decreasing by one for each loop interval:
        # For a number (variable 'num1') in a range beginning at 1, ending at 'num' plus one, and increasing by one for each loop interval:
            # Print 'num1', suppressing the usual space by utilizing the 'end' operator.
        # Print a space after each loop interval.
# End program. 

def main():
# Use a for loop to establish the range of numbers for which the loop will occur. 
    for num in range(9, 0, -1):
# Use a nested for loop to determine which numbers should be printed on each line of output. 
        for num1 in range(1, num + 1, 1):
# Display this nested loop's output, making sure to suppress the space by using the 'end' operator. 
            print(num1, end = '')
# Print a space for each line of output, which allows for one number to be eliminated from each interval of the loop. 
        print()

main()
