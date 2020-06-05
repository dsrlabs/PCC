# The following code block is written in a way where the loop will not run (comments marks are made so the code
# won't execute

# 1 age = 'x'
# 2 while age != 'x':
# 3     age = input(prompt)
# 4     print(age)
# 5     if age == 'quit':
# 6         break

# 1) figure out why exactly this loop will never run
# 2) figure out what you need to change so that this loop runs until the user enters 'quit' in the age input

# Solution
# This while loop in this code block represents an indefinite iteration. That is, the loop is executed repeatedly until
# as some condition is met, i.e. the condition is true), When the condition is false, the code proceeds to execute the
# next LOC outside of the loop.

# 1) The reasons the loop will never run because of the following:
#   a) In line 1, 'x' is assigned to the variable, age
#   b) In line 2, the variable age, is not equal to 'x' and as long as that expression is such, the loop will not execute.
#   c) In line 3, the input argument, prompt, was not defined prior to the body of the loop.
#
# 2) As shown below, the following changes were made to the code, such that loop runs until the user enters 'quit' in the age input.
#   a) Line 27 shows the variable prompt defined
#   b) The controlling expression, age, is now set to x and, by default,  as Boolean True. As long as this condition is true, the loop will begin execution.
#   c) Line 34 has the variable age now identical to the string 'quit'. It is only when the word quit is entered that the loop will break 
#      and proceed to the next LOC, it this case, nothing,

prompt = "How old are you?  "
age = 'x'
while age:
    age = input(prompt)
    print(age)
    if age == 'quit':
        break