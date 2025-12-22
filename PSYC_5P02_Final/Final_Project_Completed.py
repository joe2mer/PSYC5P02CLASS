from psychopy import visual, core, event, gui 
import csv
from random import random, choice, shuffle, uniform

# creates a dialogue box that asks the participant to enter their participant number
info = {} # creates a dictionary that will include participant number
info['participant#'] = '' # participant number is an empty string, prompting participants to enter their participant number
dlg = gui.DlgFromDict(info) # creates the dialogue box 
if not dlg.OK: # if the participant clicks cancel then the experiment will end 
    core.quit()
    
fileName = info['participant#'] # the participant number from the dialogue box will be used as the title of the csv 
dataFile = open(fileName + '.csv', 'w') # this opens the csv file for writing 
dataFile.write('phase, rt, correct, response, new_old, category\n') # writes to the csv file the following headings 


def load_csv(fname, stim_list): # creating a function that loads into the experiment the prepared csvs and the empty lists that will be appended to
    with open(fname, 'r') as f: # opens the csv in read mode  
        reader = csv.DictReader(f) # this reads the content of the csv, row by row, as a dictionary
        for row in reader: # loops through each row of the csv and appends it to a blank list 
            stim_list.append(row)

# empty lists that will be filled with the contents of the csvs being read into the experiment 
practice_stim_data = []
image_stim_data = []
recognition_practice_stim = []
recognition_stim_data = []

# loading in the csvs using the function created above
load_csv('practice_image_stim.csv', practice_stim_data)
load_csv('image_stim.csv', image_stim_data)
load_csv('practice_recognition_stim.csv', recognition_practice_stim)
load_csv('recognition_stim.csv', recognition_stim_data)

# shuffling the contents of the lists, so the stimuli are presented in a random order
shuffle(image_stim_data)
shuffle(recognition_practice_stim)
shuffle(recognition_stim_data)

# creates a window to dislplay the experiment 
win = visual.Window(size = (1024, 768), color = 'grey')

# creates a clock 
respClock = core.Clock()

# I was having issues getting the yellow flash to appear on the screen. ChatGPT recommended a rectangle that covers the width and height of the screen that could be updated.
background = visual.Rect(win, width = 2, height = 2, fillColor = 'grey')

# creates a fixation cross that will be displayed between stimuli
fix_target = visual.TextStim(win, '+')

# creates a function that displays the images from the csv and measures how quickly the participant can determine if the image is living or nonliving 
def run_encoding_trials(stim_data, save_data = True): # requires a stim_data list and whether the data will be saved as inputs.
    for image in stim_data: # loops through and displays each image in the list 
# displays a grey background with a fixation cross         
        background.fillColor = "grey"
        background.draw()
        fix_target.draw()
        win.flip()
        core.wait(1.5)
        
# changes the background color to yellow for 0.1s 
        background.fillColor = "yellow"
        background.draw()
        win.flip()
        core.wait(0.1)

# changes the background color back to grey for a period between 0.1s and 1.0s 
        background.fillColor = 'grey'
        background.draw()
        fix_target.draw()
        win.flip()
        core.wait(uniform(0.1, 1.1))


        image_path = image['image'] # retrieves the filenmae of the image
        corr = image['correct_key'] # retrieves the correct key that corresponds with the image
        image_stim = visual.ImageStim(win, image = image_path) # using the file path retrieved above we then create an image object
        category = image['category'] # retrives the category the image corresponds to 
        
# draws the image to the back buffer and then flips it to the screen
        image_stim.draw() 
        win.flip()
        respClock.reset() # resets the response clock when the image is presented 
        
# possible key responses are a, l, and escape. If a participant waits too long the key response will time out after 5 seconds
        keys = event.waitKeys(maxWait = 5.0, keyList = ['a', 'l', 'escape'])

# if no key is pressed, the response is recorded as none, reaction time as 5 seconds, and 0 for incorrect
        if keys is None:
            resp = None 
            rt = 5.00
            correct = 0
        else: # else record the response as the first key pressed and the time it took to make the key press
            resp = keys[0]
            rt = respClock.getTime()

# if the key response is the escape key then close the experiment 
        if resp == 'escape':
            win.close()
            core.quit()
 
 # if the key response is equal to the key in the csv then the response is recorded as correct
        if resp == corr:
            correct = 1
        else: # else the response is incorrect 
            correct = 0

# creates a text stimulus for feedback 
        feedback = visual.TextStim(win)

# if the participant has the correct response they will see the "correct" feedback. 
        if correct == 1:
            feedback.text = 'correct!'
        elif keys == None: # Else if no response is provided, the participant will see the "too slow" feedback.
            feedback.text = 'too slow!'
        else: # else provide them with the "incorrect" feedback
            feedback.text = 'incorrect!'

# draws the feedback to the back buffer and then flips it to the window. The feedback text appears for 0.5 seconds
        feedback.draw()
        win.flip()
        core.wait(0.5)

# if save_data was inputted as true then write to the data file 'encoding', their reaction time, whether their response was correct, their response, and the category of the image
        if save_data == True:
            dataFile.write('%s,%.3f, %i, %s, ,%s\n' % ('encoding', rt, correct, resp, category))

# this function is largely the same as the previous function. I will only be documenting the parts that are different 
# created a function that requires stim_data and whether data should be saved, displays the images, and then requires the participant to make an old/new recognition judgement 
def run_recognition_trials(stim_data, save_data = True):
    for image in stim_data:

# draws the fixation target to the back buffer and then flips it to the screen. It appears for 1.5 seconds
        fix_target.draw()
        win.flip()
        core.wait(1.5)
        
        image_path = image['image']
        corr = image['correct_key'] 
        new_old = image['new/old'] # retrieves the corresponding new/old category label for the image
        category = image['category']
        image_stim = visual.ImageStim(win, image = image_path)
        
        image_stim.draw()
        win.flip()
        respClock.reset()
        
# For the recognition task the participant is prompted to either press the s, k, or escape key. They will have 5 seconds to record a response.
        keys = event.waitKeys(maxWait = 5.0, keyList = ['s', 'k', 'escape'])

        if keys is None:
            resp = None 
            rt = 5.00
            correct = 0
        else:
            resp = keys[0]
            rt = respClock.getTime()

        if resp == 'escape':
            win.close()
            core.quit()
        
        if resp == corr:
            correct = 1
        else:
            correct = 0
        
        feedback = visual.TextStim(win)
        
        if correct == 1:
            feedback.text = 'correct!'
        elif keys == None:
            feedback.text = 'too slow!'
        else:
            feedback.text = 'incorrect!'
        
        feedback.draw()
        win.flip()
        core.wait(0.5)

# if save_data is true then write 'recognition', their reaction time, whether their response was correct, their response, and whether the image was new or old.
        if save_data == True:
            dataFile.write('%s, %.3f, %i, %s, %s, ,\n' % ('recognition', rt, correct, resp, new_old))

# create a string that will welcome the participant 
welcome = '''

Welcome to the experiment. 

In this experiment you will be shown a series of living and non-living images.When you see a living image please respond by pressing "A" on the keyboard. Otherwise, when you see a non-living image please respond by pressing "L" on the keyboard. Please respond as quickly as possible as you have a limited amount of time.

Press the spacebar to start.

'''
# creating a text stimulus using the welcome text string above
instructions = visual.TextStim(win, text = welcome)

instructions.draw()
win.flip()
event.waitKeys(keyList= ['space']) # requires the participant to press the space key to proceed

# creating a text stimulus displaying text for practice trials
practice_text = visual.TextStim(win, text = '''

This is a practice trial. Press "A" for living images and "L" for non-living images.
Try to respond as fast and accurately as possible.

Press the spacebar to start.

''')

practice_text.draw()
win.flip()
event.waitKeys(keyList= ['space'])

# Inputting the practice_stim_data list into the function. As well, as not recording data for practice trials. This runs the reaction time practice portion of the experiment.
run_encoding_trials(practice_stim_data, save_data = False)

# creating a text stimulus that explains the practice is over
intermediate_text = visual.TextStim(win, text = '''

The practice is now over. Please press spacebar to proceed to the actual experiment.

''')

intermediate_text.draw()
win.flip()
event.waitKeys(keyList= ['space'])

# inputting the image_stim_data list into the function. As well, as saving the data to the csv. This runs the actual reaction time portion of the experiment.
run_encoding_trials(image_stim_data, save_data = True)

# creates a text stimulus that explains that the 1st part of the experiment is complete
end_1st_text = '''

Please wait for the experimenter to return before continuing to the next part of the experiment 

'''

# end of the 1st part text is displayed for 5 seconds 
end_1st_instructions = visual.TextStim(win, text = end_1st_text)
end_1st_instructions.draw()
win.flip()
core.wait(5)

# creating a text stimulus displaying instructions for the second part of the experiment
Intro = visual.TextStim(win, text = '''

Welcome to the second part of the experiment.

This is a memory task. Press "s" if you have seen this image in the previous part of the experiment or
"k" if the image is new. 

Press the spacebar to start 

''')

Intro.draw()
win.flip()
event.waitKeys(keyList= ['space'])

# creating a text stimulus that displays practice instructions
practice_instruct = visual.TextStim(win, text = '''

This is a practice trial. Press the "s" key if the image is old or the "k" if the image is new.
Try to respond as fast and accurately as possible.

Press the spacebar to start. 

''')

practice_instruct.draw()
win.flip()
event.waitKeys(keyList= ['space'])

# inputting the practice recognition stim into the function. As well, as not recording data to the csv. This runs the practice recognition part of the experiment.
run_recognition_trials(recognition_practice_stim, save_data = False)

# creates a text stimulus displaying transition text between the practice and actual experiment 
intermediate_text = visual.TextStim(win, text = '''

The practice is now over. Please press spacebar to proceed to the actual experiment.

''')

intermediate_text.draw()
win.flip()
event.waitKeys(keyList= ['space'])

# inputting the recognition_stim_data into the function. As well, as writing the results to the csv. This runs the real recognition portion of the experiment where participants need to determine if an image is old or new
run_recognition_trials(recognition_stim_data, save_data = True)

# creates a text stimulus detailing the end of the experiment 
end_text = visual.TextStim(win, text = '''

The experiment is now finished. Please wait for the experimenter to return for further instructions.

''')

end_text.draw()
win.flip()
core.wait(5)

# closes the experiment 
win.close()