def rot13(string):
    '''
    This algorithm rotates each letter of the supplied string by 13 places
    '''

    result = ''

    for letter in list(string):

        if letter == ' ':
            result += ' ' 
            continue

        position  = ord(letter)

        if (position < 110) or (position < 78):
            result += chr(position + 13)
        else:
            result += chr(position - 13)

    return result

if __name__ == "__main__":

    test_string = "Jul qvq gur puvpxra pebff gur ebnq"
    expected_output = "Why did the chicken cross the road"

    if rot13(test_string) == expected_output:
        print("Success")
    else:
        print(rot13(test_string))
        print(expected_output)
        print("Failure")
