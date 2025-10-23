from psychopy import visual, core, event

# create a window

win = visual.Window(size = (1024, 768), color = "black")

# create a clock
respClock = core.Clock()

#create a fixation cross

fixation = visual.Circle(win, size = 0.05, lineColor = 'white', fillColor = 'lightGrey')

# draw the fixation cross, flip it to the screen and wait one second
fixation.draw()
win.flip()
core.wait(1.0)

# creating the string go 
GO = '''

GO!

'''

# using the string go translate it into a visual text stimulus 
present_go = visual.TextStim(win, color = 'white', text = GO, units = 'pix')

# draw the go, flip it, and reset the response clock to prepare for the trial
present_go.draw()
win.flip()
respClock.reset()

# wait for a spacebar key press and then record the time it takes to make the response
event.waitKeys(keyList= ['space'])
rt = respClock.getTime()

# string that says your reaction time was 
summary = 'Your reaction time was %.3f\n' % (rt)

# takes the summary string and turns it into a visual text stimulus
summary_text = visual.TextStim(win, text = summary, color = 'white', units = 'pix')

# draws the summary, flips it to the window and then waits for any button press
summary_text.draw()
win.flip()
event.waitKeys()
