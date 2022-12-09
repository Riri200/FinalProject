#Introduction Comments:

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
   
expInfo = {'Subject_Name':'', 'Age':'','Gender':('Male','Female')}
myDlg = gui.DlgFromDict(dictionary=expInfo,order=['Subject_Name','Age','Gender'])
expInfo['date']  = datetime.now() 
filename = (str(expInfo['Subject_Name'])+'_'+(expInfo['Age'])+'_'+(expInfo['Gender'])+ '_Results.csv')
print(filename)

nTrials=10
nBlocks=2
sub_resp = [[0]*nTrials]*nBlocks

math_equations = ['2x3=','37-29=','3x0=','24/4=','6+1=','3x3=','0x25=','18-13=','24-17=','35/7='] 
answers = [6,8,0,6,7,9,0,5,7,5] 
prob_sol = list(zip(math_equations,answers))

corr_resp = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks

for block in range(nBlocks):
    
    for trial in range(nTrials):
        prob[block][trial] = prob_sol[np.random.choice(10)]
        corr_resp[block][trial] = prob[block][trial][1]        
        print(prob[block][trial], corr_resp[block][trial])
