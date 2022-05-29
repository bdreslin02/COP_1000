# Brandon Dreslin - SPC ID# 2414755; COP1000 #4228; Module 2 Assignment
# Collaborators: none

# program2_2.py
# Program Description: Convert degrees celsius to degrees farenheit, given any temperature based on user inputs.

# Start program.
    # Get user input for a temperature in degrees celsius. Assign to variable 'celsius.'
    # Using the conversion factor, calculate the input to degrees farenheit. Assign to variable 'farenheit.'
    # Print the temperature in degrees farenheit and format to one decimal place.
# End program.

def main ():
# Prompt the user to enter a temperature in degrees celsius and assign to the celsius variable. 
    ### get user input
    celsius = int(input('Enter a temperature in degrees Celsius: '))

# Use the celsius to farenheit conversion factor to calculate the temperature in degrees farenheit.
    ### do the math
    farenheit = (celsius * 9 / 5) + 32
    ### generate output

# Display 'farenheit' to one decimal place.
    print('The temperature in degrees farenheit is', format(farenheit, '.1f'))

main()
