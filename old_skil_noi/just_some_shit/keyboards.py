import keyboard
import time
with open('game.txt','w') as game:
    game.write("it's started")
x = 10
y = 10
while True == True:

    if keyboard.read_key() == 's':
        y += 1

    if keyboard.read_key() == 'w':
        y -= 1    

    if keyboard.read_key() == 'd':
        x += 1

    elif keyboard.read_key() == 'a':
        x -= 1

    with open('game.txt','w') as game:
        render = str('\n'*y+' '*x+'*')
        game.write(render)
                
        


    # if keyboard.read_key() == 'd':
    #     c *= 1.05
    #     print(int(c)*' ', '*')
    # elif keyboard.read_key() == 'a' and c > 1:
    #     c /= 1.05
    #     print(int(c)*' ', '*')
    
