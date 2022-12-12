#Introductory Comments:
#Name: Iris Shi
#Name of the folder: 'IrisExperiment'
#Name of the file: 'IrisShi_21_Female_Results.csv'
#What my experiment does and why: This experiment looks at whether anxiety has an impact on working memory. 
      #If anxiety does have an impact on working memory then an anxiety inducing condition should impact participants ability to solve simple math equations such that it should takes participants longer and/or at a decreased accuracy to answer math equations.
      #And if working memory is impacted by anxiety we will see a slower and/or inaccurate response within the the trials of the first block and then a gradual improvement in terms of increased accuracy and response time within the trials of the second block as anxiety is gradually wearing off over time
      #Anxiety will be induced through a high arousing stimuli which will be initiated through imagining standing on a rooftop. 
      #Working memory will be measured by the accuracy and reaction times of participants answer to the math equations. 
      #Once the anxiety inducing stimuli (text) is presented, participants will press any key to move on to answer simple mathematic equations as quickly and accurately as possible. 
      #There will be 2 blocks with 10 trials each. The mathematic equations will be displayed and shuffled randomly from a list. 
      #Each mathematic equation will be displayed until participant inputs any answer/makes an attempt. Therefore, equations will be displayed for as long as it takes the participant to answer the question.  
      #Once participants have gone through the 2 blocks, a thank you text will appear for 3 seconds and the window will close.
      #Participant information and data will be collected and saved to the folder 'IrisExperiment' as a csv file which will be named as the participant's name, age, and gender followed by 'Results.csv'.
 
#importing functions and modules 
import random
import numpy as np
import pandas as pd
import os
from psychopy import visual, monitors, core, event, gui
from datetime import datetime

#path settings. Defining main directory where the experiment files are kept and data are saved
directory = os.getcwd()
path = os.path.join(directory, 'IrisExperiment')  #File name is IrisExperiment
if not os.path.exists(path):
   os.makedirs(path)

#setting up monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])

#setting up the window specs
win = visual.Window(
 fullscr=False, 
 monitor=mon, 
 size=(600,600), 
 color='grey', 
 units='pix')

#Dialogue box to collect participant info and experiment info
expInfo = {'Subject_Name':'', 'Age':'','Gender':('Male','Female')}    #created a dictionary for dialogue box that includes the variables of what info I will be collecting from participants
myDlg = gui.DlgFromDict(dictionary=expInfo,order=['Subject_Name','Age','Gender'])    #changed the order of the variables that will be presented in my dialogue box
expInfo['date']  = datetime.now() 
filename = (str(expInfo['Subject_Name'])+'_'+(expInfo['Age'])+'_'+(expInfo['Gender'])+ '_Results.csv')   #my filename will be named after what participants put into the dialogue box
print(filename)

#setting up text stimulus
anxietyText = visual.TextStim(win, text='Before the experiment begins, I would like you to imagine yourself standing on a rooftop that is very high off the ground. The rooftop is very narrow and slippery with no railings. One misstep and you will fall...!. Press any key to proceed.')
instrucText = visual.TextStim(win, text='You will now solve mathematic equations as fast and as accurate as possible. Press any key to begin block')
endText = visual.TextStim(win, text='Thank you for participating in my experiment!')
my_text=visual.TextStim(win)

#Setting up blocks, trials, and clock. There will be 2 blocks of 10 trials each
nTrials=10
nBlocks=2
rt = core.Clock()

#prefill lists for responses. To collect participant information
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks
resp_time = [[0]*nTrials]*nBlocks
trialNumbers = [[0]*nTrials]*nBlocks
blockNumbers = [[0]*nTrials]*nBlocks

#created a list of math problems to show as stimulus and created a list of answers that corresponds to each math equation
math_equations = ['2x3=','37-29=','3x0=','24/4=','6+1=','3x3=','0x25=','18-13=','24-17=','35/7='] 
answers = [6,8,0,6,7,9,0,5,7,5] 
prob_sol = list(zip(math_equations,answers))   #this matches together math equations with the corresponding correct answer

anxietyText.draw()   #drawing the first set of instructions 
win.flip()         #showing the first set of instructions 
event.waitKeys()   #will go onto the experiment once participant presses any key. waiting for keypress

#block sequence
for block in range(nBlocks):
    instrucText.draw()  #drawing instruction for the block 
    win.flip()         #showing instruction for the block
    event.waitKeys()  #will go onto the trials once participant presses any key. waiting for keypress
    
    #trial sequence
    for trial in range(nTrials):
        prob[block][trial] = prob_sol[np.random.choice(10)]   #choosing random problems from the list we had made previously
        corr_resp[block][trial] = prob[block][trial][1]      #this is the answer for the equations. It is at index 1 in the zipped list
        
        rt.reset()  #reset timing for every trial
        count=-1  #reset the counter for every trial
        
        my_text.text = prob[block][trial][0] #presenting the math equation for that trial
        my_text.draw()   #drawing the math equation for trial
        win.flip()      #showing the math equation 
        
        keys = event.waitKeys()   #will go onto the next equation once participant presses any key. Waiting for keypress of the answer to the math equation
        event.getKeys()       #Returns the list of the key that was pressed
        
        if keys:
            count=count+1  #to count up the number of times a key is pressed
                
            if count == 0:  #if this is the first time a key is pressed
                sub_resp[block][trial] = keys[0]  #get the key for the first response
                  
        #to collect and record subject accuracy
        if sub_resp[block][trial] == str(corr_resp[block][trial]):   #for correct responses the arbitrary number for accurate response is 1
            sub_acc[block][trial] = 1
            sub_resp[block][trial] = keys
            
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):    #for incorrect responses the arbitrary number for accurate response is 2
            sub_acc[block][trial] = 2
            sub_resp[block][trial] = keys            
            
        #print results. This collects participant results and records/shows math equation, correct answer, participant accuracy and their reaction time
        print('problem:', prob[block][trial], 'correct answer=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial],'subject reaction time=',rt.getTime())
endText.draw()  #drawing end of experiment text
win.flip()     #showing the end of experiment text
core.wait(3)    #presenting the end of experiment text for 3 seconds before the window is closed

#load the imported data as a variable with the corresponding output from the experiment. This collects participants info and imports info into a csv file. 
df = pd.DataFrame(data={"Block Number": blockNumbers, "Trial Number": trialNumbers,
 "Problem": prob, 
 "Answer": corr_resp, 
 "Subject Response": sub_resp, 
 "Accuracy": sub_acc, 
 "Response Time": resp_time
})
df.to_csv(os.path.join(path, filename), sep=',', index=False)   #data is saved as a csv file in the data folder I had created earlier 

#close window
win.close()
