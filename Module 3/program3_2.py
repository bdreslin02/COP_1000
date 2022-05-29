# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 3 Assignment
# Collaborators: none

# program3_2.py
# Program Description: Determine an individual's voting eligibility based on their age and U.S. citizenship status. 

# Start program.
    # Get user's input for their age. Assign to variable 'age.' 
    # If the individual is 18 years of age or older,
        # Ask the user to answer the citizen question. Assign to variable 'citizen.'
        # If the user enters 'Yes' or 'yes' as an answer,
            # Print a statement saying that they are legally allowed to vote.
        # Else,
            # Tell the user that even though they meet the age requirement, only U.S. citizens are allowed to vote.
    # Elif the user is younger than 18,
        # Tell the user that in order to vote, they must be at least 18 years old.
    # Else,
        # Catch all user input errors that may arise in the session. Tell the user to use the acceptable input answers of 'Yes' or 'yes' to the citizen question, and nothing else. 
# End program. 

def main ():
# Prompt the user to enter their age and whether or not they are a U.S. citizen. 
    age = int(input('Please enter your age: '))

# Using a nested if-elif-else statement, determine whether or not the person is of legal age to vote.
# Print statements that correspond to the user's inputs. Please refer to pseudocode for this decision structure explanation. 
    if age >= 18:
        citizen = input('Are you a United States citizen? Please answer yes or no: ')
        if citizen == 'Yes' or citizen == 'yes':
            print('You can legally vote.')
        else:
            print('You meet the age requirement. Unfortunately, you must be a U.S. citizen to vote.')
    elif age < 18:
        print('Unfortunately, you must be 18 years of age or older to vote.')
    else:
        print("Please try again. Respond 'yes' or 'no' to the citizenship question.")

main()
