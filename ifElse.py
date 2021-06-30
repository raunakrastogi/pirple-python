# Homework Assignment 3 If Else

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