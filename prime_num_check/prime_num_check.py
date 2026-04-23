# A prime number is a natural number (positive whole integer) greater than 1, 
# with only two factors (the number 1 and the number itself.)


# A factor is a number that divides another number leaving 0 as the remainder.
# example: 6 / 2 = 3 with 0 remainder

user_input = int(input("Enter a Number: "))

def check_prime(user_num):
    """ Returns True or False depending on if the value is prime.

    Parameters:
    user_num : int 
        The integer being checked for prime
    
    Returns:
    is_prime : bool
        True if prime 
        False if not prime
    """
    is_prime = True


    if user_num > 1:
        
        for divisor in range(2, user_num): # Loop runs from 2 up until 1 less than the user entered number
            
            # Factor check
            if user_num % divisor == 0: # Check if the user entered number divided by the divisor value returns no remainders
                # print(f"{divisor} is a factor")
                is_prime = False
                break
        
        return is_prime 
    else:
        return False

print(check_prime(user_input))