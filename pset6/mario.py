from cs50 import get_int

MAXHEIGHT = 8
MINHEIGHT = 1


# Takes input and rerequests it if need be.
height = get_int("Height: ")

# Casts height as int and checks to see if viable.
while MAXHEIGHT < height or height < MINHEIGHT:
    height = get_int("Height: ")


# Creates Pyramid.
for i in range(1, height + 1):

    # Prints beginning spaces. 
    for j in range(height-i):
        print(" ", end='')

# Prints left hashes.
    for k in range(height-(height-i)):
        print("#", end='')

# Prints center.
    print("  ", end='')

# Prints right hashes.
    for m in range(height-(height-i)):
        print("#", end='')
    
    print("")
    
