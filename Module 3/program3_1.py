# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 3 Assignment
# Collaborators: none

# program3_1.py
# Program Description: Based on user inputs, calculate an individual's total meal cost, entertaining the possibility of a tip.

# Start program.
    # Get user's input for the total cost of their meal. Assign to variable 'cost.'
    # Get user's input for whether or not they would like to add a tip. Assign to variable 'ask_tip.'
    # If the customer would like a tip to be added,
        # Ask them to enter the tip percent as an integer. Assign to variable 'tip.'
    # Else,
        # The tip percent is 0.
    # Using the division math operator, divide 'tip' by 100 to get the integer into a decimal form (so as to convert into a percentage), Assign to variable 'tip_percent.'
    # Calculate the actual tip amount by multiplying 'cost' and 'tip_percent' together. Assign to variable 'new_tip.'
    # Calculate the bill's total cost by adding 'cost' and 'new_tip' together. Assign to variable 'bill_total.'
    # Print the bill summary.
    # Print the person's original meal cost, formatting the result according to the currency format.
    # Print the tip amount, formatting the result according to the currency format.
    # Print the meal's total cost, formatting the result according to the currency format.
# End program. 

def main ():
# Prompt the user to enter the total cost of their meal. 
    cost = float(input('Please enter the total cost of your meal: '))
    
# Prompt the user to answer the question regarding a possible tip.
    ask_tip = input('Would you like to add a tip? Please answer yes or no. ')
    
# Use an if-else statement to determine whether a not a tip should be added to the meal's total. Prompt the user to enter an integer amount for their tip if they answered 'Yes.'
    if ask_tip == 'Yes' or ask_tip == 'yes':
        tip = int(input('Please enter the tip percent as an integer: '))
    else:
        tip = 0

# Calculate the decimal form of the integer value by dividing the tip by 100 (ensures correct math).
    ### do the math
    tip_percent = tip / 100
    ### generate output
    
# Calculate the actual tip amount by multiplying the meal's cost by the decimal form of the tip.
    ### do the math
    new_tip  = cost * tip_percent
    ### generate output
    
# Calculate the total cost of the bill by adding the cost of the meal and the tip amount together.
    ### do the math
    bill_total = cost + new_tip
    ### generate output
    
# Display the individual's bill summary, including the meal's original cost, the tip amount (if any), and the total cost of the bill. Format the results according to the currency format.
    print('Here is your bill. ')
    print('Meal cost: $', format(cost, ',.2f'), sep='')
    print('Tip amount: $', format(new_tip, ',.2f'), sep='')
    print('Total cost: $', format(bill_total, ',.2f'), sep='')

main()
