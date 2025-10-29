
# PSYC 5P02- Introduction to Programming for Psychology
## Fall 2025

### Problem Set #3

### Rubric:
* Accuracy & Efficiency: 50%
* Explanation and documentation: 50%

--- 
###  Feedback:

* rather than specifying the full path for the stimulus directory (i.e., ``C:/Users/joe2m/Desktop/PSYC5P02/PS3/stimuli/L.png"``, you could just specify it relative to where you expect the experiment file to be, i.e., ``stimuli/L.png``. That way if you have to move it to a different place the relative directories will remain the same and you don't have to replace the full path. OR, you could  create the path as a global variable, then you could specify your stimuli as something lik ``path + stimuli/L.png``
* The instructions say to use the 'T' key for target present trials but the code asks for 'Y'. 
* The stimuli locations are randomized, which I do like, but that means that stimuli can overlap which would cause problems. Is there a way you could check to make sure they don't overlap and then pick a new location if they do?
* You have basically repeated the same code for the practice and the main experiment. If you're repeating code, try to figure out if there's a way you can use a function (def) or class instead. 
* The `waitKeys()` method you used works fine, although it pauses the experiment, so if you had other things you wanted to do while waiting for a response you would want to use the `getKeys()` method and put it in a loop.
* There's probably a way to combine your accuracy and feedback into a single set of if statements -- i.e., you're checking for accuracy, setting a variable, and then checking the value of that variable a few lines later. Why not try to combine it into one set of checks?
* Similarly, your loops of creating distractors and then drawing them feels like it could have been incorporated into one single loop.
* **Overall:** Great work. Did pretty much everything I asked for, with a few small bugs. Showing progress with fundamentals. Not too much hard-coding. Try to use functions instead of repeating code. 

**Accuracy & Efficiency:** 20/25
**Explanation and documentation:** 25/25
**Total:** 45/50
          
