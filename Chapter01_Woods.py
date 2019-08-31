from subprocess import Popen
from time import sleep

#global variable for two-way branching in all current scenarios
global choice

#Function to run the next chapter based on player choice
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

#Initiated when choice results in Character Death
def Death():
    print("\t\tFATALITY\t\t")
    sleep(3.0)
    print('You have met a gruesome end within the depths of Magnolia.')
    sleep(3.0)
    print('GAME OVER')
    sleep(3.0)
    exit()

#The Beginning of the player journey in Magnolia
def TheWoods():
    print('The Woods of Magnolia are eerie in their utter silence. Even the wind appears terrified of attracting danger.\n')
    sleep(2.0)
    print('As the sole inhabitant of your camp, you remain vigilant, terrified against the creatures of the dark yet unwilling to turn your back on your self imposed quest.\n')
    sleep(3.0)
    print('A noise erupts from the bushes nearby. DO you investigate the disturbance?\nY/N?')
    i = 0
    while True:
        choice = input()
        if(choice.isalpha()):
            if(choice.lower() == 'y'):
                Bushes()
            elif (choice.lower() == 'n'):
                print('A pain flashes across your throat. You sway forward as a crimson liquid spills from your chest.\n')
                sleep(3.0)
                print('A pain erupts in your throat, panic overtaking your thoughts as you realize you are dying.\n')
                sleep(3.0)
                print('As the forest vista is replaced by the darkness of your encroaching doom, yo lament the lost opportunity to fulfill the quest haunting you for years.\n')
                sleep(3.0)
                Death()
            else:
                print('You would make a poor follower. Choose Wisely.\nY/N?')
                i += 1
        if(i>3):
            print('Four chances and you have chosen poorly. Begone from this realm\n')
            sleep(3.0)
            exit()


#If Player chooses to investigate the bushes in TheWoods()
def Bushes():
    print('Grabbing your courage, you part the bushes with a quick hand. A clearly startled fox runs away, a book on the damp ground where it once was.\n')
    sleep(3.0)
    print('Do you pick it up?\nY/N?')
    i = 0
    while True:
        choice = input()
        if (choice.lower() == 'y'):
            print('Investigation reveals the book to be a journal with plenty of missing pages and quite a few smudged with a fluid you dare not contemplate.\n')
            sleep(3.0)
            print('A mere moment before the thought of throwing the book occurs to you, the last page is flipped and you find a curiosity.\n')
            sleep(2.0)
            print('A knife no bigger than your palm and crusted in the fluid smudging the pages is stuck to the cover. Uncertain but your curiosity has driven you this far.\n')
            sleep(3.0)
            print('You pick up the knife and twirl it around towards the campfire when the chime of bells causes you to whip around, book forgotten on the forest floo and hand instinctively drawing in the knife in preparation for a struggle.\n')
            sleep(3.0)
            Meeting()
        elif (choice.lower() == 'n'):
            print('Afraid of any games on the part of shapeshifting Fae, you move back six paces and turn around only to find a surprise.\n')
            sleep(2.0)
            Meeting2()
        else:
            print('You would make a poor follower. Choose Wisely\nY/N?')
            i += 1
        if(i>3):
            print('Four chances and you have chosen poorly. Begone from this realm\n')
            sleep(3.0)
            exit()


#If player picks up knife in Bushes()
def Meeting():
    print('You freeze at the wondrous sight greeting your tired, fearful eyes.\n')
    sleep(2.0)
    print('The small campfire you built to ward off the wild wraps around the woman like a living cloak.\n')
    sleep(2.0)
    print("Yet it is the inhumanity of the woman's beauty that brings the situation into focus.\n")
    sleep(2.0)
    print('Eyes the color of a star spear into your soul as sinfully sensuous lips whisper a language utterly incomprehensible to your human ears.\n')
    sleep(4.0)
    print('You are enthralled and terrified in equal measure, the grip on the knife tightening to a painful degree. Do you attempt to harm the unexpected guest?\nY/N?')
    sleep(3.0)
    i = 0
    while True:
        choice = input()
        if(choice.isalpha()):
            if(choice.lower() == 'y'):
                print('You move swiftly to harm this creature before your soul is lost.\n')
                sleep(2.0)
                print('The knife is a hairs breadth from her bosom when a tempestual squall carries you into the nearest tree.\n')
                sleep(3.0)
                print('Your ribs and legs feel like mush and you can feel your heart threaten to break out of its cage of bones.\n')
                sleep(2.0)
                print('Ignoring the pain with hard earned familiarity, blinking your eyes brings the clearing into focus and you promptly freeze.\n')
                sleep(3.0)
                print('Standing beside the inhuman fae is a creature spoken of in hushed voices. A member of the Headless Hunt as depicted in the stories sung by mothers for children to behave.\n')
                #Function call to move onto Chapter02_Headless due to current chosen course.
                run('Chapter02_Headless.py')
            elif(choice.lower() == 'n'):
                print('Driven by your never ceasing curiosity, you are about to ask her name when you remember this is the land of Fae and names hold power.\n')
                sleep(3.0)
                print('Terrible power, espeically in the hands of these capricious creatures\n')
                sleep(3.0)
                print('Terrified of the very real capriciousness of your guest, you stand your ground with the hope of driving her away with silence.\n')
                sleep(2.0)
                print('Your hopes are dashed when the creature appears before right before your eyes without a whisper of movement and a flash of light fills your entire world for a long time after.\n')
            else:
                print('You would make a poor follower. Choose Wisely\n')
                i += 1
        if(i>3):
            print('Four chances and you have chosen poorly. Begone from this realm\n')
            sleep(3.0)
            exit()


#If player does not pick up knife in Bushes()
def Meeting2():
    print('Lips of crimson blood and skin fairer than snow brings you to a screeching halt yet before you can make a decision or even react to certain buried instincts of the psyche, crimson lips wrap around the dry flesh of your neck and darkness cloaks your vision')
    sleep(4.0)
    exit()

#Starts the game 'Behemoth'
print('Greetings adventurer\n')
sleep(3.0)
print('Do you dare to venture into the nightmare realm of the Fae?')
print('Y/N')
i = 0
while True:
    begin = input()
    if (begin.isalpha()):
        if (begin.lower() == 'y'):
            TheWoods()
        elif(begin.lower() == 'n'):
            print('Your sanity remains unchanged.', end='')
            sleep(2.0)
            print('........For now')
            sleep(2.0)
            exit()
        else:
            print('You would make a poor follower\n\n')
            i += 1
        if(i>3):
            print('Four chances and you have chosen poorly. Begone from this realm.\n')
            sleep(3.0)
            exit()
