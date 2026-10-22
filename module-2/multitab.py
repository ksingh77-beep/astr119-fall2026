#------------------------------------------------------------------------------
# This module defines multitab() a multiplication table generator.
#------------------------------------------------------------------------------
import math

def multitab(n):
    """Print multiplication table up to n.

    Parameters
    ----------
    n : positive integer scalar

    Returns
    -------
   the table
    """
    assert (type(n) is int) and (n > 0), "n must be positive integer"
    width=len(str(n*n))
    for i in range(1,n+1):
        for k in range(1,n+1):
            print(f"{i*k:{width}d}", end=' ')
        print()


    ### THIS IS WHERE YOU COME IN
    ### USE AS MANY LINES AS YOU NEED
    ### USE A FOR LOOP OR WHILE LOOP, WHICHEVER YOU LIKE
    ### YOU WILL PROBABLY NEED TO LOOK UP SOME THINGS
    ### YOU WILL DISCOVER A USEFUL OPTIONAL PARAMETER TO THE FUNCTION PRINT()


### To run as a utility
if __name__ == '__main__':
    n = int(input("Multiplication table size: "))
    multitab(n)
