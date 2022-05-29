# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 4 Assignment

# program4_2.py
# Program Description: Given a range of temperatures in degrees celsius, calculate the the corresponding temperature in degrees farenheit, and format each output in a column 8 characters wide and to one decimal place. 

# Start program.
    # Print both the celsius and farenheit temperature scales in an abbreviated format.
    # Print three equals signs, to indicate separation between the scales and the program output (up to personal preference).
    # For temperature in 'cel' in a range starting at -40, ending at 40, and increasing by 10 in each interval:
        # Use the celsius to farenheit conversion factor to determine the equivalent farenheit temperature at each interval.
        # Print 'cel' in a column 8 characters wide and to one decimal place, as well as 'fah' in a column 8 characters wide and to one decimal place.
# End program. 


def main ():
#  Display an abbreviated version of both temperature scales, as well as three equals signs to indicate separation. 
    print('     CEL      FAR')
    print('     ===      ===')
# Use a for loop with the range function to specify which numbers should be included in each interval.
# Use the temperature conversion factor to find the corresponding temperature in degrees farenheit. 
    for cel in range (-40, 41, 10):
        ### do the math
        fah = (cel * 9/5) + 32
        ### generate output
    
# Display the celsius and farenheit outputs in a column 8 characters wide and to one decimal place. 
        print(format(cel, '8.1f'), format(fah, '8.1f'))

main()
