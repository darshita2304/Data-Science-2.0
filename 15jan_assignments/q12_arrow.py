## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q12: try to explore a meaning of  "->" 

""" The -> (arrow) is used to annotate the return value for a function in 
Python 3.0 or later. It does not affect the program but is intend to be consumed 
by other users or libraries as documentation for the function."""

def velocity(s:'in miles', t:'in hours') ->'mph':
    return s/t


print (velocity(50, 5))

print(velocity.__annotations__) # to help user to input and output in proper format..
