from time import sleep
import Chapter01_Woods

def Head():
    print('"Human" You are sickened by the melodious voice of the monster of the Headless Hunt. "Keep your spirit calm and body clean for the Hunt draws near."\n')
    sleep(3.0)
    print('Before your lips part in a question you cannot fathom, the monster and the monstrously fair woman of the Fae vanish with neither senses nor the wind disturbed by their departure.\n')
    sleep(3.0)
    print('A quick attempt to glance around the clearing reveals no surprises yet you remain unnerved.\n')
    sleep(3.0)
    Chapter01_Woods.Death()

if _name_=='main()':
    Head()