from psychopy import visual, core, event, gui
from random import random, choice, shuffle

# Create a dialog box that asks for the participant number and the number of trials per condition 
info = {} # creates a dictionary that will include participant # and trials per condition
info['participant#'] = '' # empty string, prompting the participant for their input 
info ['trials_per_condition'] = ''
dlg = gui.DlgFromDict(info) # this creates the dialogue window
if not dlg.OK: # if the user presses cancel then the experiment will end 
    core.quit()

# making a csv file to save data 
fileName = info['participant#'] # using the participant # from the dialogue box as the title of the csv file
dataFile = open(fileName + '.csv', 'w') # opens the file 
dataFile.write('response, correct, rt, n_distractors, trial_type\n') # this writes to the csv file the following headers 

# create a window to display the experiment 
win = visual.Window(size = (1024, 768), color = "white")

#create a clock 
respClock = core.Clock()

# writing out the instructions that will be presented to the participants 
welcome = '''

Welcome to the Visual Search Task.

In this experiment you will need to find the letter T amongst a group of distractors.

When the letter T is present press y on the keyboard as fast as possible.

If the letter T is not present press n on the keyboard. 

Press the spacebar to begin. 
'''

# This is done to actually present the instructions 
instructions = visual.TextStim(win, color = 'black', text = welcome, units = 'pix')

instructions.draw() # draws the instructions to the back buffer 
win.flip() # flips the stimulus to the screen 
event.waitKeys(keyList= ['space']) # requires the participant to press the spacebar to proceed

# Creating practice instructions in string format 
practice = '''

Let us begin with some practice trials. 

Press the spacebar to start practice

'''

# creating a text stimulus using the practice string up above 
practice_instructions = visual.TextStim(win, color = 'black', text = practice, units = 'pix')
practice_instructions.draw() # draws the stimulus to the back buffer
win.flip() # flips the stimulus to the screen 
event.waitKeys(keyList= ['space']) # requires the participant to press the spacebar to proceed

# creating a list that includes 4 different orientations that the T and L.png will take on 
ori_random = [0, 90, 180, 270]

# As the practice trial is very similar to the actual experiment I will only be commenting on the the steps that differ from the main experiment

# created a for loop that will loop through three times 
for trial in range(3):
        practice_trial = True # confirms to me that this is a practice_trial. This is used later in the experiment to distinguish practice trials from the main experiment when we input it into the csv
        show_target = random() < 0.5
        
        if show_target == False: # if the target is not present than 9 Ls will appear else only 8 will appear 
            n_distractor_stim = 8 + 1
        else:
            n_distractor_stim = 8
            
        
        image_stims = []

        for i in range(n_distractor_stim):
            image_stim = visual.ImageStim(win, image= "C:/Users/joe2m/Desktop/PSYC5P02/PS3/stimuli/L.png",
                pos = (random()-0.5, random()-0.5),
                size = (0.05, 0.05),
                ori = choice(ori_random)
                )
                
            image_stims.append(image_stim)

        for image_stim in image_stims:
            image_stim.autoDraw = True 
            

        if show_target:
            target = visual.ImageStim(win, image = "C:/Users/joe2m/Desktop/PSYC5P02/PS3/stimuli/T.png",
            pos = (random() -0.5, random()-0.5),
            size = (0.05, 0.05),
            ori = choice(ori_random)
            )
        else: 
            target = None

        if target:
            target.autoDraw = True 

        win.flip()
        respClock.reset()
            
        keys = event.waitKeys(maxWait = 5.0, keyList = ['y', 'n', 'escape'])
        
        if keys is None:
            resp = None 
            rt = 5.00
            corr = 0
        else:
            resp = keys[0]
            rt = respClock.getTime()
            
        if resp == 'y' and show_target == True:
            corr = 1
        elif resp == 'n' and show_target == False:
            corr = 1
        else:
            corr = 0
            
        if resp == 'escape':
            win.close()
            core.quit()
            
        feedback = visual.TextStim(win, color= 'black')
        
        if corr == 1:
            feedback.text = 'correct!'
        elif keys == None:
            feedback.text = 'too slow!'
        else:
            feedback.text = 'incorrect!'
         
         
        for image_stim in image_stims:
            image_stim.autoDraw = False
        if target:
            target.autoDraw = False
            
        feedback.draw()
        win.flip()
        core.wait(0.5)
        
        if practice_trial:
            trial_type = 'practice'
        else:
            trial_type = 'main'
        
        dataFile.write('%s,%i,%.3f,%i,%s\n' % (resp, corr, rt, n_distractor_stim, trial_type))

# creating a string that indicates the practice has finished 
end = '''

Practice is finished.

Once you press the spacebar the real experiment will begin. 

'''

# creating a text stimulus using the end string above 
end_text = visual.TextStim(win, color = 'black', text = end, units = 'pix')

end_text.draw()
win.flip()
event.waitKeys(keyList= ['space'])

# taking the number the participant enters into the dialogue box for trials per condition and converts it from a string to an integer type
trials_per_condition = int(info['trials_per_condition'])

# creating variables that will be populated during the main trials of the experiment 
main_correct = 0 # number of trials a participant gets correct 
main_rts = [] # creating a list that will include all of the reaction times 
main_total = 0 # total number of trials a participant completes 

ori_random = [0, 90, 180, 270]

# creating a list of the number of distractors a participant will see during the experiment 
list_distractors = [8, 12, 14]

# using the shuffle function from psychopy's random package to randomize the order that participants will see each of the different set sizes  
shuffle(list_distractors)

# creating a for loop that loops through each of the items in the list of distractors
for n_image_stim in list_distractors:

# nesting within our for loop another for loop that iterates over the number of trials per condition. The number of trials per condition is determined by the number the participant inputs into the dialogue box 
    for trial in range(trials_per_condition):
        practice_trial = False # this just indicates that this is not a practice trial. Again, this will be used later This is used later in the experiment to distinguish practice trials from the main experiment when we input it into the csv 
        show_target = random() < 0.5 # using the random function we decide that the T.png will have a 50% chance of appearing on each trial 
        
        if show_target == False: # if the target is not present add 1 to the number of distractors else leave unchanged 
            n_distractor_stim = n_image_stim + 1
        else:
            n_distractor_stim = n_image_stim + 0
            
# created an empty list to store distractor stimuli on the current trial         
        image_stims = []

# creating a for loop that loops through, creating a certain number of distractors per trial 
        for i in range(n_distractor_stim):
            image_stim = visual.ImageStim(win, image= "C:/Users/joe2m/Desktop/PSYC5P02/PS3/stimuli/L.png",
                pos = (random()-0.5, random()-0.5), # use the random function to randomize the position of the distractors. Then -0.5 is used to center the stimuli so they are not going off screen
                size = (0.05, 0.05), 
                ori = choice(ori_random) # use the choice function to randomize the orientation of the distractors. This is used over shuffle because shuffle only randomly reorders the entire list whereas choice picks a random item from the list
                )
# appending the distractors to the empty list 
            image_stims.append(image_stim)

# creating a for loop that loops through, drawing each of the distractors in the image_stims list to the back buffer
        for image_stim in image_stims:
            image_stim.autoDraw = True 
            

# if show_target is true, then display the T.png, else do not display the target 
        if show_target:
            target = visual.ImageStim(win, image = "C:/Users/joe2m/Desktop/PSYC5P02/PS3/stimuli/T.png",
            pos = (random() -0.5, random()-0.5),
            size = (0.05, 0.05),
            ori = choice(ori_random)
            )
        else: 
            target = None

# if target is present, draw the target to the backbuffer 
        if target:
            target.autoDraw = True 

        win.flip()
        
# resets the clock when presenting a stimulus 
        respClock.reset()

# waits 5 seconds for a key response. Possible key responses are y, n, and escape 
        keys = event.waitKeys(maxWait = 5.0, keyList = ['y', 'n', 'escape'])

# if no key is pressed within the allotted time. Records the response as none, reaction time as 5 seconds, and incorrect, else take the first key inputted and the time it is associated with
        if keys is None:   
            resp = None 
            rt = 5.0
            corr = 0
        else:
            resp = keys[0]
            rt = respClock.getTime()

# if response is y and the target is present the participant is correct, else if the response is n and the target is not present the participant is correct, else the participant is incorrect
        if resp == 'y' and show_target == True:
            corr = 1
        elif resp == 'n' and show_target == False:
            corr = 1
        else:
            corr = 0

# if the participant preses the escape key the experiment will close      
        if resp == 'escape':
            win.close()
            core.quit()


# creating a text stimulus for feedback 
        feedback = visual.TextStim(win, color= 'black')

# if the participant is correct provide them with the feedback text correct, else if no keys are pressed provide them with the feedback text too slow, else provide them with the feedback text incorrect 
        if corr == 1:
            feedback.text = 'correct!'
        elif keys == None:
            feedback.text = 'too slow!'
        else:
            feedback.text = 'incorrect!'
         

# creates a for loop that loops through turning off each of the distractors in the image_stims list 
        for image_stim in image_stims:
            image_stim.autoDraw = False

# if target is present turn off the presence of the target 
        if target:
            target.autoDraw = False
            
        feedback.draw()
        win.flip()
        
# feedback remains up for half a second
        core.wait(0.5)

# if a practice_trial is show, trial type will be recorded as practice in the csv, else trial type will be recorded as main in the csv, total number of trials will increase by 1, the number correct will increase each time the participant gets a trial correct, and reaction times are appended to the main_rts list 
        if practice_trial:
            trial_type = 'practice'
        else:
            trial_type = 'main'
            main_total += 1
            main_correct += corr 
            main_rts.append(rt)
   
# writes the response, whether it is correct, reaction time, number of distractors, and the trial type to the csv file    
        dataFile.write('%s,%i,%.3f,%i,%s\n' % (resp, corr, rt, n_distractor_stim, trial_type))

# closes the data file 
dataFile.close()

# if the participant has performed more than 0 trials, calculate the accuracy of the participant by taking the number of correct trials divided by the total number and multiply by 100 else return an accuracy of 0
accuracy = (main_correct / main_total) * 100 if main_total > 0 else 0

# calculating reaction time by taking the sum of the reaction time list and dividing it by the length of the list
avg_rt = sum(main_rts) / len(main_rts) 

# creating a string that will mention the accuracy and reaction time of the participant 
summary = ' Your accuracy was %.1f, Your reaction time was %.3f\n' % (accuracy, avg_rt)

# creating a text stimulus using the summary string above 
summary_text = visual.TextStim(win, text = summary, color = 'black', units = 'pix')

summary_text.draw()
win.flip()

# takes any key to end the experiment 
event.waitKeys()

# videos and resources used to supplement learning 
# https://www.youtube.com/watch?v=0dJgLf7BxbE
# https://www.youtube.com/watch?v=e2ZO8UiNa_E
# https://workshops.psychopy.org/3days/day3/builder_parallel/makingMassComponents.html
