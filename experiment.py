#Introductory Comments:

import random
import numpy as np
import pandas as pd
import os
from psychopy import visual, monitors, core, event
from psychopy import gui
from datetime import datetime

directory = os.getcwd()
path = os.path.join(directory, 'IrisExperiment')
if not os.path.exists(path):
   os.makedirs(path)

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])

win = visual.Window(
 fullscr=False, 
 monitor=mon, 
 size=(600,600), 
 color='grey', 
 units='pix'
)
   
expInfo = {'Subject_Name':'', 'Age':'','Gender':('Male','Female')}
myDlg = gui.DlgFromDict(dictionary=expInfo,order=['Subject_Name','Age','Gender'])
expInfo['date']  = datetime.now() 
filename = (str(expInfo['Subject_Name'])+'_'+(expInfo['Age'])+'_'+(expInfo['Gender'])+ '_Results.csv')
print(filename)

anxietyText = visual.TextStim(win, text='Before the experiment begins, I would like you to imagine yourself standing on a rooftop that is very high off the ground. The rooftop is very narrow and slippery with no railings. One misstep and you will fall...!')
instrucText = visual.TextStim(win, text='You will now solve mathematic equations as fast and as accurate as possible. Press any key to begin block')
fixation = visual.TextStim(win, text='+', color='black')

nTrials=10
nBlocks=2
my_text=visual.TextStim(win)
sub_resp = [[0]*nTrials]*nBlocks

sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks

math_equations = ['2x3=','37-29=','3x0=','24/4=','6+1=','3x3=','0x25=','18-13=','24-17=','35/7='] 
answers = [6,8,0,6,7,9,0,5,7,5] 
prob_sol = list(zip(math_equations,answers))

anxietyText.draw()
win.flip()
event.waitKeys()

rt_clock = core.Clock()
cd_timer = core.CountdownTimer()

for block in range(nBlocks):
    instrucText.draw()
    win.flip()
    event.waitKeys()
      
    for trial in range(nTrials):
        prob[block][trial] = prob_sol[np.random.choice(10)]
        corr_resp[block][trial] = prob[block][trial][1]        
        
        rt_clock.reset()
        cd_timer.add(3)
            
        event.clearEvents(eventType='keyboard')
         
        count=-1
        while cd_timer.getTime() > 0:
            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            keys = event.getKeys
            
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1
      
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2
            
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])

win.close()
