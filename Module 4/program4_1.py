# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 4 Assignment
# Collaborators: None

# program4_1.py
# Program Description: Given user inputs for a specified range of numbers, test for even and odd numbers. Then, display the results to the user. 

# Start program.
    # Begin an even number counter that reports the number of even integers within the specified range. Assign to variable 'even.'
    # Begin an odd number counter that reports the number of odd integers within the specified range. Assign to variable 'odd.'
    # Begin a total number counter that reports the total number of both 'even' and 'odd' within the specified range. Assign to variable 'total.'
    # Get user's input for the starting integer that will help to define the loop's range. Assign to variable 'start_num.'
    # Get user's input for the ending integer that will help to define the loop's range. Assign to variable 'end_num.'
    # For variable 'num' in the range of 'start_num' and 'end_num + 1' (add one to include 'end_num' in the calculations):
        # If the remainder of 'num' is equivalent to zero (use remainder math operator to test this condition):
            # Continue to add one to 'even.'
            # Continue to add 'num' to 'total.'
        # Else:
            # The number is odd, so continue to add one to 'odd.'
            # Continue to add 'num' to 'total.'
    # Print a summary of the calculations, and tell the user how many even and odd integers are found within the specified range.
    # Print a statement telling the user the summation of all integers, both even and odd.
# End program.

def main ():
# Begin the even number counter and set it equal to 0. 
    even = 0
    
# Begin the odd number counter and set it equal to 0.
    odd = 0
    
# Begin the total number counter and set it equal to 0. 
    total = 0
    
# Prompt the user to enter their desired starting integer and ending integer for the loop.
    ### get user input
    start_num = int(input('Please enter the starting integer for this loop: '))
    ### get user input
    end_num = int(input('Please enter the ending integer for this loop: '))
    
# Use a foor loop with a range function to determine the range for which the even/odd calculation should test for. 
    for num in range(start_num, end_num + 1):
        
# Use the remainder math operator and divide 'num' by 2. If the output equals 0, the number is even. 
        ### do the math
        if num % 2 == 0:
        ### generate output
            
            ### do the math
            even += 1
            ### generate output
            
            ### do the math
            total += num
            ### generate output
            
# There is no need to test for odd numbers, since all other numbers that are not even must be odd. 
        else:
            ### do the math
            odd += 1
            ### generate output

            ### do the math
            total += num
            ### generate output
    
# Display a summary of the test, telling the user (a) the number of even integers, (b) the number of odd integers, and (c) the total of all integers when added together. 
    print('Found', even, 'even integers and', odd, 'odd integers.')
    print('The total of all integers is', total)

main()
    
            
            
