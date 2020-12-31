// Imports libraries and establishes main class.
#include <stdio.h>
#include <cs50.h>

int main()
{
    // Gets height input.
    int height = get_int("Height: ");

    // Tests input validity.
    while (height > 8 || height < 1)
    {
        height = get_int("Height: ");
    }

    // Creates for loop to make structure.
    for (int i = 0; i < height; i++)
    {
        // Prints spaces.
        for (int h = (height - (height - (i + 1))); h < height; h++)
        {
            printf(" ");
        }

        // Print hashes.
        for (int j = (height -  i); j < height; j++)
        {
            printf("#");
        }

        // Prints final hash.
        printf("#\n");
    }

}