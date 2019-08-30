#Choice Statement applicable to all dialogue only events
while True:
    i = 0
    choice = input()
    if (choice.isalpha()):
        if (choice.lower() == 'y'):
            XXX()
        elif (choice.lower() == 'n'):
            print('')
            XXX()
        else:
            print('')
            i += 1
            if (i > 3):
                print('You are worthless. Begone from here')
                XXX(3.0)
                exit()