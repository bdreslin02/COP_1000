# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 5 Assignment #1
# Collaborators: None

# program5_1.py
# Program Description: Based on user inputs, calculate the necessary fields - subtotal, tax, and total - using a separate function to process the calculations.
    # 'Return' these outputs, "catch" them in the 'main' function, and report these values to the user, with all fields properly formatted in currency format. 

# Start program ➞ Begin with defining the program's 'main' function.
    # Prompt the user to enter the price of the item they are intending to purchase; the price may be a floating-point number. Assign to variable 'price.'
    # Prompt the user to enter the quantity of the item they are intending to purchase. Assign to variable 'quantity.'
    # Prompt the user to enter whether or not a seven percent (7%) sales tax is applicable to the item they are intending to purchase. 
    # "Catch" the output of the 'checkout' function for the arguments 'price,' 'quantity,' and 'tax.' Assign to variable 'subtotal, tax, total.'
    # Print a statement telling the user that a summary of their bill will be displayed.
    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
    # Print a statement summarizing both (a) how many units of the item they are purchasing and (b) the per item price, formatting the price in currency format.
    # Print a statement telling the user what their subtotal was calculated to be.
    # Print a statement telling the user what the amount of tax (if any) was calculated to be. If tax is inapplicable, '$0.00' will be shown, denoting that no sales tax was calculated.
    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
# Define the 'checkout' function for parameters 'price,' 'quantity,' and 'tax' (these parameters will replace the arguments 'subtotal,' 'tax,' and 'total' in this function), which will be called in the 'main' function when the program executes.
    # Calculate the item's subtotal by using the multiplication math operator to multiply 'price' by 'quantity.' Assign to variable 'subtotal.'
    # Calculate the item's tax (if applicable) by using the multiplication math operator to multiply 'subtotal' by '0.07' (7% sales tax converted to a decimal). Assign to variable 'tax.'
    # Calculate the visit's total payable price by using the addition math operator to add 'subtotal' to 'tax.' Assign to variable 'total.'
    # 'Return' all three (3) variables - 'subtotal,' 'tax,' and 'total' - to the 'main' function. This is where 'main' will "catch" the output and print the results to the user.
# End program.

# Define the 'main' function. This is where the majority of the program's processing will occur. 
def main():
    
# Get user's input for the price of the item they are intending to purchase. 
    price = float(input('Enter the price of the item you are purchasing: '))
    
# Get user's input for the quantity of the item they are intending to purchase. 
    quantity = int(input('How many units of this item are you purchasing? '))
    
# Get user's input for whether or not a 7% sales tax is applicable to the item being purchased. 
    tax = input("Is this item subject to a 7% sales tax? Please enter 'y' or 'n': ")
    
# Using the so-called 'dot-notation,' "catch" the 'checkout' function's output by calling it for the arguments 'price,' quantity,' and 'tax.' Assign to variable 'subtotal, tax, total.'
    subtotal, tax, total = checkout(price, quantity, tax)
    
# Display a statement telling the user that a summary of their bill will follow.
    print('Here is your bill:')
    
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('------------------')
    
# Display a statement that tells the user (a) the amount of the item they are purchasing and (b) the per item price of the item they are purchasing. 
    print('You are purchasing ', quantity, ' units of the same item, with a per item price of $', format(price, ',.2f'), sep = '')
    
# Display a statement that shows the user the calculated subtotal (i.e., the total without the addition of sales tax). 
    print('Subtotal: $', format(subtotal, ',.2f'), sep = '')
    
# Display a statement that shows the user the calculated tax (if applicable). 
    print('Tax: $', format(tax, ',.2f'), sep = '')
    
# Display a statement that tells the user the total payable amount (i.e., the total with the addition of sales tax). 
    print('Please pay $', format(total, ',.2f'), sep = '')
    
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('------------------')
    
# Define a new function that will utilize three parameters (the 'main' function's arguments) to calculate and 'return' the fields necessary for the user to pay their amount due. 
def checkout(price, quantity, tax):
    
# Calculate the visit's subtotal by multiplying 'price' by 'quantity.'
    subtotal = price * quantity
    
# Calculate the visit's tax (if any) by multiplying 'subtotal' by '0.07.'
    tax = subtotal * 0.07
    
# Calculate the visit's total payable amount by adding 'subtotal' to 'tax.'
    total = subtotal + tax
    
# 'Return' the above variables to the 'main' function, so that 'main' can "catch" them and report each variable's values to the user. 
    return subtotal, tax, total

# Call the 'main' function to end the program. 
main()
    
