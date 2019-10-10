import re


def PassWord():
    """Checking the input text according to the rules"""
    info = 'Your password must contain digits and letters in both registers only.'
    print(info)
    text = input()
    while len(text) < 8:
        print('Your password must be 8 symbols long at least. Please try again.')
        text = input()
    else:
        intext = re.compile(r'''(
                               (?=.*[0-9].*)  # At least one digit
                               (?=.*[a-z].*)  # At least one letter 
                               (?=.*[A-Z].*)  # At least one capitalize letter
                               [0-9a-zA-Z]    # Text contains digits and letters in both registers
                                )''', re.VERBOSE)
        if bool(intext.match(text)) == True:
            print('That\'s fine')
        else:
            PassWord()


