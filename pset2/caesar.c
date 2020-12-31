// Imports libraries and define main class with commandline arguments.
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[])
{

    // Tests input to see if valid.
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!(isdigit(argv[1][i])))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Acknowledges input as valid.
    printf("Success\n%i\n", argc);

    // Takes input and defines variables.
    string input = get_string("plaintext: ");
    int len = strlen(input);
    int key = atoi(argv[1]);

    // Begins returned statement.
    printf("ciphertext: ");

    // Encrypts plaintext, turns it into ciphertext.
    for (int i = 0; i < len; i++)
    {
        if (input[i] >= 'A' && input[i] <= 'Z')
        {
            printf("%c", (((input[i] - 'A') + key) % 26) + 'A');
        }

        else if (input[i] >= 'a' && input[i] <= 'z')
        {
            printf("%c", (((input[i] - 'a') + key) % 26) + 'a');
        }

        else if (input[i] == ' ')
        {
            printf(" ");
        }

        else
        {
            printf("%c", input[i]);
        }

    }

    // Prints newline.
    printf("\n");





}