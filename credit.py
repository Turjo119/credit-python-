from cs50 import get_int
from cs50 import get_string

# User input Credit Card Number
CC = get_int("Enter Credit Card Number: ")

# Check for valid number of digits
digits = len(str(CC))
if digits < 13 or digits > 16 or digits == 14:
    print("Invalid")
    exit(1)

elif digits == 13 or digits == 15 or digits == 16:
    #Variables for use
    tmp0 = CC
    tmp1 = CC
    sum0 = 0
    sum1 = 0
    total_sum = 0
    rmd0 = 0
    rmd1 = 0
    special = 0

    # Lund's algorithm step 1
    while(tmp0 != 0):
        rmd0 = ((tmp0 / 10) % 10) * 2
        tmp0 = tmp0 / 100

        if (rmd0 > 0 or rmd0 < 9):
            sum0 = sum0 + rmd0
        else:
            special = sum0 + special

    print (f"sum0 is {sum0} ")

    # Lund's algorithm step 2
    while (tmp1 != 0):
        rmd1 = (tmp1 / 100) % 10
        tmp1 = tmp1 / 100
        sum1 = sum1 + rmd1

    print(f"sum1 is {sum1}")
    total_sum = sum0 + sum1
    print(f"total_sum is {total_sum}")

    # Check for valid number
    if (int(total_sum % 10) == 0):
        print("CARD IS VALID")
    else:
        print("CARD IS INVALID")

