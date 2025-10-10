from psychopy import visual, core, event 
win = visual.Window([400,400])
message = visual.TextStim(win, text ='hello')
message2 = 


message.autoDraw = True 

timer = core.Clock() # instance of a clock 
mouse = event.Mouse(visible=True)

x, y = 0.0

startTime = timer.getTime() # what is the current time 

while timer.getTime() - startTime < 20.0: # I want an event to last a certain amount of time 
    x += 0.1 # update position by 0.1 each loop 
    y += 0.1
    message.pos = [x, y]
    message.draw() # draw each frame 
    win.flip()
    
    
while timer.getTime() - startTime < 20.0: # I want an event to last a certain amount of time 
    x = mouse.getPos()[0] 
    y = mouse.getPos()[1] # indexing the x, y coordinates 
    message.pos = [x, y]
    message.draw() # draw each frame 
    win.flip()