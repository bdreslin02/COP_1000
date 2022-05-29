# Brandon Dreslin - SPC ID# 2414755; COP1000 #4228; Module 2 Assignment
# Collaborators: none

# program2_3.py
# Program Description: Calculate both the area and perimeter of a rectangle, given any number based on user inputs.

# Start program.
    # Get user input for the length of the rectangle. Assign to variables 'length.'
    # Get user input for the width of the rectangle. Assign to variable 'width.'
    # Using area and perimeter formulas for a rectangle, calculate the results for both variables. Assign the variables to 'area' and 'perimeter,' respectfully.
    # Print two different statements: one for the outputs of both the area and the perimeter. Format the former to two decimal places, and the latter to three decimal places.
# End program.

def main ():
# Prompt user to enter length and width dimensions in inches and assign to the 'length' and 'width' variables, respectfully.
    ### get user input
    length = float(input('Enter the length dimension in inches: '))
    width = float(input('Enter the width dimension in inches: '))
    
# Use the area and perimeter formulas of a rectangle to calculate for 'area' and 'perimeter.' 
    ### do the math
    area = length * width
    perimeter = 2 * (length + width)
    ### generate output
    
# Display 'area' in sqaured inches and 'perimeter' in inches, formatting the former to two decimal places and the latter to three decimal places.
    print('The area of this rectangle is', format(area, '.2f'), 'squared inches')
    print('The perimeter of this rectangle is', format(perimeter, '.3f'), 'inches')

main()
       
