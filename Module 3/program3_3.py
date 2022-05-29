# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 3 Assignment
# Collaborators: none

# program3_3.py
# Program Description: Give the user a quiz, where they will have to enter their answers either as a decimal, an integer, or as a string. Based on their answers, provide feedback to the user. Finally, display their final quiz score. 

# Start program.
# Define variable 'score' as 0. This variable will change once the user begins the quiz.
# Get user's inputs for the sine of 45 degrees. Assign to variable 'sin45.'
# If the user inputs either '0.7071' or '.7071,'
    # Print a congratulation statement.
    # Add one point to their total score.
# Else,
    # Print a feedback statement.
# Get user's input for the year during which the "Miracle on the Hudson" emergency landing occurred. Assign to variable 'miracle.'
# If the user inputs the year '2009,'
    # Print a congratulation statement.
    # Add another point to their total score.
# Else,
    # Print a feedback statement.
# Get user's input for the answer to the riddle. Assign to variable 'riddle.'
# If the user answers 'post office' (in any capitalization format),
    # Print a congratulation statement.
    # Add another point to their total score.
# Else,
    # Print a feedback statement.
# Print a score summary, using 'score' to display the individual's total.
# If the total score is 3,
    # Print a 'great' feedback statement.
# Else, if the total score is 2,
    # Print an 'not bad' feedback statement.
# Else,
    # Print a 'bad' feedback statement.
# Print a statement thanking the user for taking the quiz.
# End program. 

def main ():
# Define the user's starting score of 0. 
    score = 0

# Prompt the user to input the sine value of 45 degrees (as a decimal). 
# Use an if-else statement to determine whether or not their answer is correct.
# Display feedback statements according to the user's answer.
# Add 1 to the user's score, if necessary. 
    sin45 = float(input('To four decimal places, please enter the sine value for 45 degrees: '))
    if sin45 == 0.7071 or sin45 == .7071:
        print("Great job! Paying attention in trigonometry wasn't a waste of your time!")
        score += 1
    else:
        print('Good try. The answer is 0.7071.')

# Prompt the user to input the year during which this event occurred (as an integer). 
# Use an if-else statement to determine whether or not their answer is correct.
# Display feedback statements according to the user's answer.
# Add 1 to the user's score, if necessary.
    miracle = int(input('In what year did the so-called "Miracle on the Hudson" water landing occur? '))
    if miracle == 2009:
            print('Amazing! Captain Sully is glad you got this question correct.')
            score += 1
    else:
        print('Better luck next time. This emergency landing happened in 2009, where a US Airways plane crash landed onto the Hudson River in New York.')

# Prompt the user to input the answer to this riddle.
# Use an if-else statement to determine whether or not their answer is correct.
# Display feedback statements according to the user's answer.
# Add 1 to the user's score, if necessary.
    riddle = input('What starts with a P, ends with an E, and has thousands of letters? ')
    if riddle == 'Post Office' or riddle == 'Post office' or riddle == 'post office':
        print('Your riddle-solving skills are sharp! Give yourself a pat on the back!')
        score += 1
    else:
        print("The answer is the 'post office.' Seems so obvious now, doesn't it?")
        
# Display the user's score summary.
# Display feedback statements based on the score they earned.
# Display a final statement thanking the user for taking the quiz. 
    print('You earned a total score of', score, 'out of 3.')
    if score == 3:
        print('Perfect score! Keep it up.')
    elif score == 2:
        print('So close! Maybe next time.')
    else:
        print('Good attempt. You will do better next time.')

    print('Thank you taking this quiz!')

main ()
