# implementation of card game - Memory

import simplegui
import random
turns = 0

# helper function to initialize globals
def new_game():
    global deck, exposed, turns, flips, flip1, flip2
    flips = 0
    turns = 0
    flip1 = None
    flip2 = None
    deck = 2 * range(1, 9)
    random.shuffle(deck)
    exposed = [False for num in deck]
          
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, turns, flips, flip1, flip2
    if not exposed[pos[0]//50]:
        if flips == None or flips == 0:
            exposed[pos[0]//50] = True
            flip1 = pos[0] // 50
            flips = 1
#            print flip1, flip2, "flips: ", flips
        elif flips == 1: 
            exposed[pos[0]//50] = True
            flip2 = pos[0] // 50
            flips = 2
            turns += 1
#            print flip1, flip2, "flips: ", flips
        else:
            if deck[flip1] != deck[flip2]:
                exposed[flip1] = False
                exposed[flip2] = False              
            exposed[pos[0]//50] = True  
            flips = 1
            flip1 = pos[0] // 50
            flip2 = None
#            print flip1, flip2, "flips: ", flips
    return turns
                           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global turns
    width = 25
    for num in range(len(deck)):
        if exposed[num]:
            canvas.draw_text(str(deck[num]), ((num * 50)+ 10, 70), 50, 'Red')
        else:
            canvas.draw_image(image, (413 / 2, 620 / 2), (413, 620), ((num * 50)/2 + width, 100/2), (50, 100))
        width += 25
        
    label.set_text("Turns = " + str(turns))    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
image = simplegui.load_image('https://image.shutterstock.com/image-vector/playing-card-back-side-600w-90984266.jpg')
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
