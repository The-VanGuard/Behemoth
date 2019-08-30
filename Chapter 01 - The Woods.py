from time import sleep

global choice
#global hp
#global mana

def Death():
    print('You have met the fate of many foolish souls wandering into the depths of Magnolia')
    sleep(3.0)
    exit()

def TheWoods():
    print('The Woods of Magnolia are too silent for this time of night.')
    sleep(2.0)
    print('As the sole inhabitant of your camp, you remain vigilant, terrified against the creatures of the dark yet unwilling to turn your back on your self imposed quest')
    sleep(3.0)
    print('You hear a noise. DO you investigate the disturbance?')
    i = 0
    while True:
        choice = input()
        if(choice.isalpha()):
            if(choice.lower() == 'y'):
                Bushes()
            elif (choice.lower() == 'n'):
                print('A pain flashes across your throat and eyes.')
                Death()
            else:
                print('You would make a poor follower. Choose Wisely')
                i += 1
        if(i>3):
            print('You are worthless. Begone from here')
            sleep(3.0)
            exit()


def Bushes():
    print('When you part the bush, a fox is startled and runs away, leaving a book on the ground')
    sleep(1.0)
    print('Do you pick it up?')
    i = 0
    while True:
        choice = input()
        if (choice.lower() == 'y'):
            print('The book turns out to be a tattered journal.Upon opening it, Opening the book reveals a curio of a knife embedded into the pages')
            sleep(3.0)
            print('You pick up the knife and twirl it around towards the campfire when a human gasp causes you to whip around, knife at the ready')
            sleep(2.0)
            Meeting()
        elif (choice.lower() == 'n'):
            print('You walk back to camp and find yourself confronted with a blade to your eye')
            Death()
        else:
            print('You would make a poor follower. Choose Wisely')
            i += 1
        if(i>3):
            print('You are worthless. Begone!!!')
            sleep(3.0)
            exit()

def Meeting():
    print('You freeze at the sight of the utterly beautiful woman before you')
    sleep(3.0)
    print('Nay. You realize her skin is too fair, her hair too smooth, her proportions perfect beyond any human reckoning')
    sleep(3.0)
    print('Eyes the color of a star spear into your soul as sinfully sensuous lips whisper a language utterly incomprehensible to your human ears')
    sleep(4.0)
    print('You are enthralled and terrified in equal measure. You have a knife in your hand. Do you attempt to harm your inhuman guest?')
    sleep(3.0)
    i = 0
    while True:
        choice = input()
        if(choice.isalpha()):
            if(choice.lower() == 'y'):
                print('You move swiftly to harm this creature before your soul is lost')
                sleep(2.0)
                print('Your knife is a hairs breadth from her bosom when a tempestual squall carries you into the nearest tree')
                sleep(3.0)
                print('Your ribs and legs feel like mush and you can feel your heart threaten to break out of its cage of bones.')
                sleep(2.0)
                print('Ignoring the pain with hard earned familiarity, blinking your eyes brings the clearing into focus and you promptly freeze.')
                sleep(3.0)
                print('Standing beside the inhuman fae is a creature spoken of in hushed voices in quiet corners for fear of summoning it. A member of the Headless Hunt as depicted in the books')
                sleep(4.0)
                exit()
            elif(choice.lower() == 'n'):
                print('You are about to ask her name when you remember this is the land of Fae where names have power')
                sleep(2.0)
                print('Terrified of the very real capriciousness of your guest, you stand your ground with the hope of driving her away with silence.')
                sleep(2.0)
                print('Your hopes are dashed when the creature appears before right before your eyes without a whisper of movement and a flash of light brightens your peripherals')
            else:
                print('You would make a poor follower. Choose Wisely')
                i += 1
        if(i>3):
            print('You are worthless. Begone!!!')
            sleep(3.0)
            exit()



print('Greetings adventurer\n')
sleep(5.0)
print('Do you dare to venture into the nightmare realm of the Fae?')
print('Y/N')
i = 0
while True:
    begin = input()
    if (begin.isalpha()):
        if (begin.lower() == 'y'):
            TheWoods()
        elif(begin.lower() == 'n'):
            print('Sane you are.......\n Wahahahaha')
            exit()
        else:
            print('You would make a poor follower')
            i += 1
        if(i>3):
            print('You are worthless. Begone!!!')
            exit()

