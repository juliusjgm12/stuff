# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 01:23:45 2018

@author: julius
"""

with open("My Story", 'r') as f:
    for line in f:
        if line != "Q":
            print line
        else:
            