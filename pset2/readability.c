//Gets libraries and establishes main class.
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
    // Gets input.
    string input = get_string("Text: ");

    // Initializes variables.
    float words = 1;
    float letters = 0;
    float sentences = 0;
    int len = strlen(input);

    // Creates for loop to check every letter of input.
    for (int i = 0; i < len; i++)
    {
        // Counts letters.
        if (isalpha(input[i]))
        {
            letters++;

        }

        // Counts words.
        else if (isspace(input[i]))
        {
            words++;

        }

        // Counts Sentences
        else if (input[i] == '.' || input[i] == '?' || input[i] == '!')
        {
            sentences++;

        }
    }

    // Defines variables that represent rates.
    float l = letters / words * 100;
    float s = sentences / words * 100;

    // Defines result of formula as variable and rounds it/
    float index = .0588 * l - .296 * s - 15.8;
    int grade = round(index);

    // Returns grade level and accounts for out of bounds errors.
    if (grade >= 1 && index <= 16)
    {
        printf("Grade %i\n", grade);
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");

    }
    else
    {
        printf("Before Grade 1\n");

    }






}