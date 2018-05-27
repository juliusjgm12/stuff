# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:54:39 2018

@author: julius
"""
# TEST WINDOW FOR PYGLET TESTING
# WINDOW WILL OPEN FOR 10 SECONDS AND CLOSE AUTOMATICALLY

from psychopy import visual, core

time = core.getTime()

testWindow = visual.Window([400,400], name='test', colorSpace='rgb',color=[-1,-1,-1], units='pix')
testCircle = visual.Circle(win=testWindow, radius=20, edges=32, units='pix', lineColor=(0,0,0), fillColor=(0,0,0))
testCircle.setPos([0,0])
while (core.getTime() - time) < 10:
    testCircle.draw()
    testWindow.flip()
testWindow.close()