#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // User input of CC number
    long CC = get_long("Enter Credit Card Number: ");
    long store = CC; // for later use

    //Check for correct number of digits
    int counter = 0; // counting no. of digits
    int a; // variable for reasons
    for (counter = 0; store != 0; counter ++)
    {
        a = store % 10;
        store = store / 10;
    }
    printf(" Number of digits: %i\n", counter);
    int name = counter; // to find the name of the card

    if ((counter < 13) || (counter > 16))
    {
        printf("INVALID\n");
        return 0;
    }

    else if ((counter = 13) || (counter = 15) || (counter = 16))
    {
        long store2 = CC; // for later use
        int sum1 = 0; // for every other digit 2nd-to-last
        int sum2 = 0; // remaining digits
        int sum3 = 0; // total sum
        int rmdr; // remainder from every other digit 2nd-to-last
        int special; // for product digits greater than 9

        // Seperating every other digit

        for (int c = 0; store2 != 0; c++)
        {
            rmdr = ((store2 / 10) % 10) * 2;
            store2 = store2 / 100;
            if (rmdr > 0 && rmdr < 9)
            {
                sum1 = sum1 + rmdr;
            }

            else
            {
                special = (rmdr / 10) + (rmdr % 10);
                sum1 = sum1 + special;

            }

        }
        // For the remaining digits
        long store3 = CC; // for later use
        int rmdr2; //  for remaining digits
        for (int d = 0; store3 != 0; d++)
        {
            rmdr2 = (store3 % 100) % 10;
            store3 = store3 / 100;
            sum2 = sum2 + rmdr2;
        }

        sum3 = sum1 + sum2;
        printf("sum1 = %i\n", sum1);
        printf("sum2 = %i\n", sum2);
        printf("sum3 = %i\n", sum3);

        if (sum3 % 10 == 0)
        {
            printf("VALID\n");
        }

        else
        {
            printf("INVALID\n");
            return 0;
        }

        long store4 = CC;// for later use
        // AMEX,VISA OR MASTERCARD
        if (name ==  15)
        {
            int x = store4 / 10000000000000;
            printf("x is %i\n", x);
            if ((x == 34) || (x == 37))
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }

        }
        else if (name == 16)
        {
            int x = store4 / 100000000000000;
            printf("x is %i\n", x);
            if ((x >= 51) && (x <= 55))
            {
                printf("MASTERCARD\n");
            }
            else if ((x >= 40) && (x <= 49))
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (name == 13)
        {
            int x = store4 / 100000000000;
            printf("x is %i\n", x);
            if ((x >= 40) && (x <= 49))
            {
                printf("VISA\n");
            }
        }
    }
}
