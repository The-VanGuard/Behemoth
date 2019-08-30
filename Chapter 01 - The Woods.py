from time import sleep

global choice
#global hp
#global mana

def Death():
    print('You have met the fate of many foolish souls wandering into the depths of Magnolia')
    sleep(3.0)
    exit()

def TheWoods():
    print('The Woods of Magnolia are far too silent.')
    sleep(2.0)
    print('As the sole inhabitant of your camp, you remain vigilant, terrified against the creatures of the dark yet unwilling to turn your back on your self imposed quest')
    sleep(3.0)
    print('A noise erupts from the bushes nearby. DO you investigate the disturbance?')
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
    print('Grabbing your courage, you part the bushes with a quick hand. A clearly startled fox runs away, a book on the damp ground where it once was.')
    sleep(3.0)
    print('Do you pick it up?')
    i = 0
    while True:
        choice = input()
        if (choice.lower() == 'y'):
            print('Investigation reveals the book to be a journal with plenty of missing pages and quite a few smudged with a fluid you dare not contemplate.')
            sleep(3.0)
            print('A mere moment before the thought of throwing the book occurs to you, the last page is flipped and you find a curiosity')
            sleep(2.0)
            print('A knife no bigger than your palm and crusted in the fluid smudging the pages is stuck to the cover. Uncertain but your curiosity has driven you this far.')
            sleep(3.0)
            print('You pick up the knife and twirl it around towards the campfire when the chime of bells causes you to whip around, book forgotten on the forest floo and hand instinctively drawing in the knife in preparation for a struggle.')
            sleep(3.0)
            Meeting()
        elif (choice.lower() == 'n'):
            print('Afraid of any games on the part of shapeshifting Fae, you move back six paces and turn around only to find a surprise.')
            sleep(2.0)
            Meeting2()
        else:
            print('You would make a poor follower. Choose Wisely')
            i += 1
        if(i>3):
            print('You are worthless. Begone!!!')
            sleep(3.0)
            exit()

def Meeting():
    print('You freeze at the wondrous sight greeting your tired, fearful eyes.')
    sleep(2.0)
    print('The small campfire you built to ward around wild animals wraps around the woman like a living cloak')
    sleep(2.0)
    print("Yet it is the inhumanity of the woman's beauty that brings the situation into focus")
    sleep(2.0)
    print('Eyes the color of a star spear into your soul as sinfully sensuous lips whisper a language utterly incomprehensible to your human ears')
    sleep(4.0)
    print('You are enthralled and terrified in equal measure, the grip on the knife tightening to a painful degree. Do you attempt to harm the unexpected guest?')
    sleep(3.0)
    i = 0
    while True:
        choice = input()
        if(choice.isalpha()):
            if(choice.lower() == 'y'):
                print('You move swiftly to harm this creature before your soul is lost')
                sleep(2.0)
                print('The knife is a hairs breadth from her bosom when a tempestual squall carries you into the nearest tree')
                sleep(3.0)
                print('Your ribs and legs feel like mush and you can feel your heart threaten to break out of its cage of bones.')
                sleep(2.0)
                print('Ignoring the pain with hard earned familiarity, blinking your eyes brings the clearing into focus and you promptly freeze.')
                sleep(3.0)
                print('Standing beside the inhuman fae is a creature spoken of in hushed voices. A member of the Headless Hunt as depicted in the stories sung by mothers for children to behave')
                sleep(4.0)
                exit()
            elif(choice.lower() == 'n'):
                print('Driven by your never ceasing curiosity, you are about to ask her name when you remember this is the land of Fae where names have power')
                sleep(3.0)
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


def Meeting2():
    print('Lips of crimson blood and skin fairer than snow brings you to a screeching halt yet before you can make a decision or even react to certain buried instincts of the psyche, crimson lips wrap around the dry flesh of your neck and darkness cloaks your vision')
    sleep(4.0)
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

