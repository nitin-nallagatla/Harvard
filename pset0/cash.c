#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main()
{
// Initializing Constants
    float QUARTERS = 25;
    float DIMES = 10;
    float NICKELS = 05;
    float PENNIES = 01;

// Gets Change Input, and rerequests if necessary.
    int coins = 0;
    double money = get_float("Change owed? ");

// Tests Change input, and rerequests if necessary.
    while (money < 0)
    {
        money = get_float("Change owed? ");

    }

// Rounds money value to begin operation.
    money *= 100;

    money = round(money);

// Checks maximum amount of quarters usable.
    while (money >= QUARTERS)
    {
        money -= QUARTERS;
        coins += 1;
    }

// Checks maximum amount of dimes usable after quarters.
    while (money >= DIMES)
    {
        money -= DIMES;
        coins += 1;
    }

// Checks maximum amount of nickels usable after dimes.
    while (money >= NICKELS)
    {
        money -= NICKELS;
        coins += 1;
    }

// Checks maximum amount of pennies usable after nickels.
    while (money >= PENNIES)
    {
        money -= PENNIES;
        coins += 1;
    }

// Returns output.
    printf("%i\n", coins);







}