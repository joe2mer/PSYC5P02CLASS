# Lecture 5 Notes

#Psychopy Basics

# Works on principle of double buffering 
# process of flipping things from the back buffer onto the primary display

# Psychopy Coder View 

# Couple of different views, coder, builder, etc. 

# can import psychopy into juptyrnotebooks or spyder via: pip install python 
# need to create a monitor if you are working in jupyter or spyder 

# Let's make a really simple experiment 

from psychopy import visual, core # import psychopy library. Importing specific methods from the psychopy library 
win = visual.Window([400,400]) # creating a window to draw to. Identifier could be anything outside of win. Here we are defining the size of the window 
message = visual.TextStim(win, text= 'hello') # drawing a stimulus to the back buffer. Every object you draw we need to assign a label. 
message.autoDraw = True # automatically draw every frame. Autodraw tells us that it is going to automatically draw every frame. 
win.flip() # flips the stimulus to the screen. Everything up until this point has been done on the back buffer 
core.wait(2.0) # delay the next event from happening. None of the downstream stuff happens until 2 seconds later 
message.text = 'world' #change properties of exisiting stim. Modify the properties of the stmulus by calling the handle 
win.flip() # flip it again 
core.wait(2.0) # wait two seconds 

# can change units of visual.Window. Currently in pix (i.e., units = pix)

#posner cueing task 

from psychopy import visual, event, core, data
win = visual.Window([1024, 768], fullscr = False, units = 'pix')
# initialize some stimuli
fixation = visual.Circle(win, size = 5,
    lineColor = 'white', fillColor = 'lightGrey')
    
respClock = core.Clock()

probe = visual.GratingStim(win, size = 80, 
    pos = [300, 0],
    tex = None, mask = 'gauss',
    color = 'green')
cue = visual.ShapeStim(win, 
    vertices = [[-30, -20], [-30,20], [30, 0]], 
    lineColor = 'red', fillColor = 'salmon')
info = {}
info['fixTime'] = 0.5
info['cueTime'] = 0.2
info['probeTime'] = 0.2

for trial in range(5):
    fixation.draw()
    win.flip()
    core.wait(info['fixTime'])

    cue.draw()
    win.flip()
    core.wait(info['cueTime'])

    fixation.draw()
    probe.draw()
    win.flip()
    # core.wait(info['probeTime']) no longer waiting 
    
    respClock.reset() # reset my clock
    
    win.flip() # clear screen 
    
    #look for a keyboard response 
    keys = event.waitKeys(keyList = ['left', 'right', 'escape'])
    resp = keys[0]
    rt = respClock.getTime()
    
    #calculate accuracy
    if (resp == 'left' and side[0] == 2) or (resp == 'right' and side[0] ==1):
        corr = 1
    else:
        corr = 0 

# writing files 

#fileID = open(filename, 'w')
# w = write, x = open, a = append
# do this before the experiment begins 

# %i = integer, %.3f = floating integer with 3 decimal places

# Global Keys

# if anyone presses the q key its going to quit the experiment 

#if in need of finding something put in psychopy --














