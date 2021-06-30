# Homework Assignment 3 If Else
"""
Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.


Extra Credit:

Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function:

6,5,"5"

You should modify it so that it returns true instead of false.

Hint: there's a built in Python function called "int" that will help you convert strings to Integers.
"""
def Compare(f1,f2,f3):
    if (int(f1) == int(f2)) or (int(f1) == int(f3)) or (int(f2) == int(f3)):
        return True
    else:
        return False

print(Compare(1,2,2)) 
print(Compare(1,1,3))
print(Compare(3,4,3))
print(Compare(1,2,3))

# Extra Credit
print(Compare(5,6,"5"))
