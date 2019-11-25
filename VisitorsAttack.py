#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on November 25, 2019, at 12:00
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
#***************************************************************************************/
#*    Title: WhenVisitorsAttack source code
#*    Author: Schroer, J
#*    Date: 2019
#*    Code version: 1.0
#*    Availability: http://github.com/jschroer26/VisitorsAttack
#*
#***************************************************************************************/
#
from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'laser1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jschro26\\Documents\\Research\\Research_EEG\\EEG Experiments\\laser1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
Introduction = visual.TextStim(win=win, name='Introduction',
    text='Welcome to\n\nWhen Visitors Attack!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startup = visual.TextStim(win=win, name='startup',
    text="Visitors from the Plant Shape have landed on our planet.\n\nThey have found laser guns that only work when reflected off a mirror.\nThey don't know how to fire their weapons so, they need your help.\n\n\nPress A to continue...",
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Intro2"
Intro2Clock = core.Clock()
Pressthis = visual.TextStim(win=win, name='Pressthis',
    text='In the first part of the game, press A or B to show the Visitors\nwhere their laser beam will hit.\nYou will receive no feedback in this section, but keep firing, the\nVisitors are learning.\n\nPress A when you are ready to start the game.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
Visitor = visual.ImageStim(
    win=win,
    name='Visitor', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Part_Deux"
Part_DeuxClock = core.Clock()
Welcome2 = visual.TextStim(win=win, name='Welcome2',
    text='Great Job!\nThe visitors know how their laser guns work, now they want\nto show you.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Setup = visual.TextStim(win=win, name='Setup',
    text="In this section of the game, the Visitors will show you how their \nlaser guns fire. You will receive an image of the laser's path.\n\n\nRemember to press only A or B to say where the laser beam will hit.\n\n\nGood Luck!\n\nPress A when you are ready to continue.\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
fbimage = visual.ImageStim(
    win=win,
    name='fbimage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Feedbackimg"
FeedbackimgClock = core.Clock()
fbimage1 = visual.ImageStim(
    win=win,
    name='fbimage1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Part_Trois"
Part_TroisClock = core.Clock()
Reflectionfbtext = visual.TextStim(win=win, name='Reflectionfbtext',
    text='Amazing Job!\nNow you and the Visitors know how their laser guns work!\n\nThe Visitors think that you are ready for the Challenge Round...\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text="The Visitors are ready to really test themselves, and they\nthink you are ready, too.\n\nIn the last round, you will be challenged with more mirrors,\nand different mirror set-ups. These set-ups will be controlled\nby the Visitor's Mothership.\nBe careful, and do your best!\n\nPress 'a' to continue...",
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "ChallengeRound"
ChallengeRoundClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Finalities"
FinalitiesClock = core.Clock()
Finalscreen = visual.TextStim(win=win, name='Finalscreen',
    text='What a great job!\n\nThe Visitors are so happy that you came to the lab today\nand played their game with them.\nThey hope you had fun.\n\nThanks for playing!\n\nGoodbye.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
WelcomeComponents = [Introduction, startup, key_resp_3]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Introduction* updates
    if Introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Introduction.frameNStart = frameN  # exact frame index
        Introduction.tStart = t  # local t and not account for scr refresh
        Introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Introduction, 'tStartRefresh')  # time at next scr refresh
        Introduction.setAutoDraw(True)
    if Introduction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Introduction.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            Introduction.tStop = t  # not accounting for scr refresh
            Introduction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Introduction, 'tStopRefresh')  # time at next scr refresh
            Introduction.setAutoDraw(False)
    
    # *startup* updates
    if startup.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        startup.frameNStart = frameN  # exact frame index
        startup.tStart = t  # local t and not account for scr refresh
        startup.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startup, 'tStartRefresh')  # time at next scr refresh
        startup.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['a', 'A'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Introduction.started', Introduction.tStartRefresh)
thisExp.addData('Introduction.stopped', Introduction.tStopRefresh)
thisExp.addData('startup.started', startup.tStartRefresh)
thisExp.addData('startup.stopped', startup.tStopRefresh)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro2"-------
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
Intro2Components = [Pressthis, key_resp_4]
for thisComponent in Intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Intro2"-------
while continueRoutine:
    # get current time
    t = Intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pressthis* updates
    if Pressthis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pressthis.frameNStart = frameN  # exact frame index
        Pressthis.tStart = t  # local t and not account for scr refresh
        Pressthis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pressthis, 'tStartRefresh')  # time at next scr refresh
        Pressthis.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['A', 'a'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro2"-------
for thisComponent in Intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Pressthis.started', Pressthis.tStartRefresh)
thisExp.addData('Pressthis.stopped', Pressthis.tStopRefresh)
# the Routine "Intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practicetrials = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\\\..\\\\Research_EEG\\\\EEG Experiments\\\\visattackprac1.xlsx'),
    seed=None, name='Practicetrials')
thisExp.addLoop(Practicetrials)  # add the loop to the experiment
thisPracticetrial = Practicetrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
if thisPracticetrial != None:
    for paramName in thisPracticetrial:
        exec('{} = thisPracticetrial[paramName]'.format(paramName))

for thisPracticetrial in Practicetrials:
    currentLoop = Practicetrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
    if thisPracticetrial != None:
        for paramName in thisPracticetrial:
            exec('{} = thisPracticetrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Practice"-------
    # update component parameters for each repeat
    Visitor.setImage(visitors)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    PracticeComponents = [Visitor, key_resp]
    for thisComponent in PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Practice"-------
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Visitor* updates
        if Visitor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Visitor.frameNStart = frameN  # exact frame index
            Visitor.tStart = t  # local t and not account for scr refresh
            Visitor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Visitor, 'tStartRefresh')  # time at next scr refresh
            Visitor.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['A', 'B', 'a', 'b'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys.append(theseKeys.name)  # storing all keys
                key_resp.rt.append(theseKeys.rt)
                # was this 'correct'?
                if (key_resp.keys == str(corrans)) or (key_resp.keys == corrans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practicetrials.addData('Visitor.started', Visitor.tStartRefresh)
    Practicetrials.addData('Visitor.stopped', Visitor.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for Practicetrials (TrialHandler)
    Practicetrials.addData('key_resp.keys',key_resp.keys)
    Practicetrials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        Practicetrials.addData('key_resp.rt', key_resp.rt)
    Practicetrials.addData('key_resp.started', key_resp.tStartRefresh)
    Practicetrials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practicetrials'

# get names of stimulus parameters
if Practicetrials.trialList in ([], [None], None):
    params = []
else:
    params = Practicetrials.trialList[0].keys()
# save data for this loop
Practicetrials.saveAsExcel(filename + '.xlsx', sheetName='Practicetrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Part_Deux"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
Part_DeuxComponents = [Welcome2, Setup, key_resp_2]
for thisComponent in Part_DeuxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Part_DeuxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Part_Deux"-------
while continueRoutine:
    # get current time
    t = Part_DeuxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Part_DeuxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome2* updates
    if Welcome2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome2.frameNStart = frameN  # exact frame index
        Welcome2.tStart = t  # local t and not account for scr refresh
        Welcome2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome2, 'tStartRefresh')  # time at next scr refresh
        Welcome2.setAutoDraw(True)
    if Welcome2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Welcome2.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            Welcome2.tStop = t  # not accounting for scr refresh
            Welcome2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Welcome2, 'tStopRefresh')  # time at next scr refresh
            Welcome2.setAutoDraw(False)
    
    # *Setup* updates
    if Setup.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        Setup.frameNStart = frameN  # exact frame index
        Setup.tStart = t  # local t and not account for scr refresh
        Setup.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Setup, 'tStartRefresh')  # time at next scr refresh
        Setup.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['a', 'b'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_DeuxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_Deux"-------
for thisComponent in Part_DeuxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome2.started', Welcome2.tStartRefresh)
thisExp.addData('Welcome2.stopped', Welcome2.tStopRefresh)
thisExp.addData('Setup.started', Setup.tStartRefresh)
thisExp.addData('Setup.stopped', Setup.tStopRefresh)
# the Routine "Part_Deux" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
feedbacktrials = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\\\..\\\\Research_EEG\\\\EEG Experiments\\\\visattackprac2.xlsx'),
    seed=None, name='feedbacktrials')
thisExp.addLoop(feedbacktrials)  # add the loop to the experiment
thisFeedbacktrial = feedbacktrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFeedbacktrial.rgb)
if thisFeedbacktrial != None:
    for paramName in thisFeedbacktrial:
        exec('{} = thisFeedbacktrial[paramName]'.format(paramName))

for thisFeedbacktrial in feedbacktrials:
    currentLoop = feedbacktrials
    # abbreviate parameter names if possible (e.g. rgb = thisFeedbacktrial.rgb)
    if thisFeedbacktrial != None:
        for paramName in thisFeedbacktrial:
            exec('{} = thisFeedbacktrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Feedback"-------
    # update component parameters for each repeat
    fbimage.setImage(visitors)
    key_resp_5.keys = []
    key_resp_5.rt = []
    # keep track of which components have finished
    FeedbackComponents = [fbimage, key_resp_5]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fbimage* updates
        if fbimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fbimage.frameNStart = frameN  # exact frame index
            fbimage.tStart = t  # local t and not account for scr refresh
            fbimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fbimage, 'tStartRefresh')  # time at next scr refresh
            fbimage.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['a', 'b'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_5.keys.append(theseKeys.name)  # storing all keys
                key_resp_5.rt.append(theseKeys.rt)
                # was this 'correct'?
                if (key_resp_5.keys == str(corrans)) or (key_resp_5.keys == corrans):
                    key_resp_5.corr = 1
                else:
                    key_resp_5.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    feedbacktrials.addData('fbimage.started', fbimage.tStartRefresh)
    feedbacktrials.addData('fbimage.stopped', fbimage.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           key_resp_5.corr = 1;  # correct non-response
        else:
           key_resp_5.corr = 0;  # failed to respond (incorrectly)
    # store data for feedbacktrials (TrialHandler)
    feedbacktrials.addData('key_resp_5.keys',key_resp_5.keys)
    feedbacktrials.addData('key_resp_5.corr', key_resp_5.corr)
    if key_resp_5.keys != None:  # we had a response
        feedbacktrials.addData('key_resp_5.rt', key_resp_5.rt)
    feedbacktrials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    feedbacktrials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedbackimg"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    fbimage1.setImage(feedback)
    # keep track of which components have finished
    FeedbackimgComponents = [fbimage1]
    for thisComponent in FeedbackimgComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackimgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Feedbackimg"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackimgClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackimgClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fbimage1* updates
        if fbimage1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fbimage1.frameNStart = frameN  # exact frame index
            fbimage1.tStart = t  # local t and not account for scr refresh
            fbimage1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fbimage1, 'tStartRefresh')  # time at next scr refresh
            fbimage1.setAutoDraw(True)
        if fbimage1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2.5-frameTolerance:
                # keep track of stop time/frame for later
                fbimage1.tStop = t  # not accounting for scr refresh
                fbimage1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fbimage1, 'tStopRefresh')  # time at next scr refresh
                fbimage1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackimgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedbackimg"-------
    for thisComponent in FeedbackimgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    feedbacktrials.addData('fbimage1.started', fbimage1.tStartRefresh)
    feedbacktrials.addData('fbimage1.stopped', fbimage1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'feedbacktrials'

# get names of stimulus parameters
if feedbacktrials.trialList in ([], [None], None):
    params = []
else:
    params = feedbacktrials.trialList[0].keys()
# save data for this loop
feedbacktrials.saveAsExcel(filename + '.xlsx', sheetName='feedbacktrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Part_Trois"-------
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
Part_TroisComponents = [Reflectionfbtext, text, key_resp_6]
for thisComponent in Part_TroisComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Part_TroisClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Part_Trois"-------
while continueRoutine:
    # get current time
    t = Part_TroisClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Part_TroisClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Reflectionfbtext* updates
    if Reflectionfbtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Reflectionfbtext.frameNStart = frameN  # exact frame index
        Reflectionfbtext.tStart = t  # local t and not account for scr refresh
        Reflectionfbtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Reflectionfbtext, 'tStartRefresh')  # time at next scr refresh
        Reflectionfbtext.setAutoDraw(True)
    if Reflectionfbtext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Reflectionfbtext.tStartRefresh + 4.5-frameTolerance:
            # keep track of stop time/frame for later
            Reflectionfbtext.tStop = t  # not accounting for scr refresh
            Reflectionfbtext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Reflectionfbtext, 'tStopRefresh')  # time at next scr refresh
            Reflectionfbtext.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['a', 'b'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_TroisComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_Trois"-------
for thisComponent in Part_TroisComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Reflectionfbtext.started', Reflectionfbtext.tStartRefresh)
thisExp.addData('Reflectionfbtext.stopped', Reflectionfbtext.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "Part_Trois" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
crtrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\\\..\\\\Research_EEG\\\\EEG Experiments\\\\visattackprac3.xlsx'),
    seed=None, name='crtrials')
thisExp.addLoop(crtrials)  # add the loop to the experiment
thisCrtrial = crtrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCrtrial.rgb)
if thisCrtrial != None:
    for paramName in thisCrtrial:
        exec('{} = thisCrtrial[paramName]'.format(paramName))

for thisCrtrial in crtrials:
    currentLoop = crtrials
    # abbreviate parameter names if possible (e.g. rgb = thisCrtrial.rgb)
    if thisCrtrial != None:
        for paramName in thisCrtrial:
            exec('{} = thisCrtrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ChallengeRound"-------
    # update component parameters for each repeat
    image.setImage(visitors)
    key_resp_7.keys = []
    key_resp_7.rt = []
    # keep track of which components have finished
    ChallengeRoundComponents = [image, key_resp_7]
    for thisComponent in ChallengeRoundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ChallengeRoundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ChallengeRound"-------
    while continueRoutine:
        # get current time
        t = ChallengeRoundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChallengeRoundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['a', 'b'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_7.keys == []:  # then this was the first keypress
                    key_resp_7.keys = theseKeys.name  # just the first key pressed
                    key_resp_7.rt = theseKeys.rt
                    # was this 'correct'?
                    if (key_resp_7.keys == str(corrans)) or (key_resp_7.keys == corrans):
                        key_resp_7.corr = 1
                    else:
                        key_resp_7.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChallengeRoundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ChallengeRound"-------
    for thisComponent in ChallengeRoundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    crtrials.addData('image.started', image.tStartRefresh)
    crtrials.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           key_resp_7.corr = 1;  # correct non-response
        else:
           key_resp_7.corr = 0;  # failed to respond (incorrectly)
    # store data for crtrials (TrialHandler)
    crtrials.addData('key_resp_7.keys',key_resp_7.keys)
    crtrials.addData('key_resp_7.corr', key_resp_7.corr)
    if key_resp_7.keys != None:  # we had a response
        crtrials.addData('key_resp_7.rt', key_resp_7.rt)
    crtrials.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    crtrials.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "ChallengeRound" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'crtrials'

# get names of stimulus parameters
if crtrials.trialList in ([], [None], None):
    params = []
else:
    params = crtrials.trialList[0].keys()
# save data for this loop
crtrials.saveAsExcel(filename + '.xlsx', sheetName='crtrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Finalities"-------
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
FinalitiesComponents = [Finalscreen]
for thisComponent in FinalitiesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinalitiesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Finalities"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinalitiesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinalitiesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Finalscreen* updates
    if Finalscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Finalscreen.frameNStart = frameN  # exact frame index
        Finalscreen.tStart = t  # local t and not account for scr refresh
        Finalscreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Finalscreen, 'tStartRefresh')  # time at next scr refresh
        Finalscreen.setAutoDraw(True)
    if Finalscreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Finalscreen.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            Finalscreen.tStop = t  # not accounting for scr refresh
            Finalscreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Finalscreen, 'tStopRefresh')  # time at next scr refresh
            Finalscreen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinalitiesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finalities"-------
for thisComponent in FinalitiesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Finalscreen.started', Finalscreen.tStartRefresh)
thisExp.addData('Finalscreen.stopped', Finalscreen.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
