# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 5 Assignment #2 (CUSTOM MODULE)

# grades.py
# ** CUSTOM MODULE FOR MODULE 5 ASSIGNMENT #2**

'''
This is a custom module that is imported into 'program5_2.py.'
The following two (2) custom functions are called in the program.
This first function is used within the program to (a) keep counters of both how many tests are within each course and the total score of all the user's test grades, (b) determine how many times the 'for' loop should occur, and (c) return the average of each test score within the given course.
To pass the argument 'temp' to the above program's 'main' function, we use 'temp' as this function's parameter.
The second function is OPTIONAL and is not required for the assignment; however, the grade determiner will help the user to better understand their final term grade.
To pass the argument 'term_avg' to the above program's 'main' function, we use 'term_avg' as this function's parameter. 
In addition, both functions are considered a 'value-returning' function, meaning that they return the calculations as a variable, which will then be called in the program's 'main' function.
'''

def grade_pct(course):                                                                          # Define the 'grade_pct' function for the 'course' argument.
    tests = 0                                                                                   # Allow the 'tests' counter to equal 0, which will be used again later in the function. 
    score_total = 0                                                                             # Allow the 'score_total' counter to equal 0, which will be used again later in the function. 

    num_tests = int(input('Please enter the number of tests in this course: '))                 # Get user's input for the number of test scores present within the specified course.  

    for test in range (1, num_tests + 1):                                                       # Use a 'for' loop to determine the range of numbers for which the loop should execute its processes.
        tests += 1                                                                              # Continue to add 1 to the 'tests' counter ➞ This will later be used as one variable for calculating each course average. 
        test_score = float(input('Please enter the score for test ' + str(tests) + ': '))       # Get user's input for each individual test score within the specified course ➞ The number of scores depends on the user's previous input.
        score_total += test_score                                                               # Continue to add 'test_score' to the 'score_total' counter ➞ This ensures that the calculations for each course average is correct. 

    return (score_total / tests)                                                                # Using the division math operator, divide 'score_total' by 'tests' and 'return' this number. In the program, the 'main' function will catch this returned value and display the result to the user. 

def determine_grade(term_avg):                                                                  # Define the 'determine_grade' function for the 'term_avg' argument.
    if term_avg >= 90:                                                                          # Use an 'if' statement to determine whether 'term_avg' is greater than or equal to 90.
        return 'A'                                                                              # 'Return' a grade of 'A' if the above statment is tested to be true. 
    elif term_avg >= 80:                                                                        # Use an 'elif' statement to determine whether 'term_avg' is greater than or equal to 80.
        return 'B'                                                                              # 'Return' a letter grade of 'B' if the above statment is tested to be true. 
    elif term_avg >= 70:                                                                        # Use an 'elif' statement to determine whether 'term_avg' is greater than or equal to 70.
        return 'C'                                                                              # 'Return' a letter grade of 'C' if the above statment is tested to be true. 
    elif term_avg >= 60:                                                                        # Use an 'elif' statement to determine whether 'term_avg' is greater than or equal to 60.
        return 'D'                                                                              # 'Return' a letter grade of 'D' if the above statment is tested to be true. 
    else:                                                                                       # All other grades are less than 60.
        return 'F'                                                                              # 'Return' a letter grade of 'F' for all other numerical grades. 
