# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 2 Assignment
# Collaborators: none

# program2_1.py
# Program Description: Calculate regular weekly pay (ignoring overtime), given user inputs.
# NOTE: This program assumes that there are five days in any given work week. Vacation days and sick days are not considered.

# Start program.
    # Get user input for the number of hours worked during the week. Assign to variable 'hrs_worked.'
    # Get user input for the hourly pay rate. Assign to variable 'hrly_pay.'
    # Calculate the weekly pay by multiplying the hours worked and the hourly pay together. Assign to variable 'wkly_pay.'
    # Print the weekly pay and format to two decimal places, ensuring that a comma separates values above one thousand dollars.
# End program.

def main ():
# Prompt user to enter both the number of hours they worked during the week and their hourly pay.
    ### get user input
    hrs_worked = float(input('Enter the number of hours you worked this week: '))
    hrly_pay = float(input('Enter your hourly pay rate: '))
    
# Calculate their weekly pay by multiplying both variables together.
    ### do the math
    wkly_pay = hrs_worked * hrly_pay
    ### generate output
    
# Display 'wkly_pay,' in dollars, to two decimal places, ensuring that any amount above one thousand dollars is correctly separated by commas.
    print('Your weekly pay is $', format(wkly_pay, ',.2f'), sep='')

main()
