# raw_input
def get_input( prompt ):
    value = raw_input( prompt )
    for letter in value:
        if letter < "a" or letter > "z":
            print( "The character", letter, "is not allowed!")
            #value = get_input( prompt ) # DO NOT DO THIS!
    return value

s = get_input( "Give a string of lower case letters: " )
print( "The user entered:", s )

d = input( "Give a nember: " )
print( "The user entered:", d )
