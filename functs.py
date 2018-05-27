# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 00:53:39 2018

@author: julius
"""

class functions(object):
    def __init__(self):
        pass
    
    def printtimes(self, msg, num):
        for i in range(0, num):
            print msg
    def stocks(self, prices):
        low = 0
        high = 0
        diff = 0
        topDiff = 0
        for i in prices:
            for j in prices[i + 1:]:
                if j <= i:
                    continue
                else:
                    diff = j - i
                if diff > topDiff:
                    topDiff = diff
                    low = i
                    high = j
        return {"Profit": topDiff, "Buy": low, "Sell": high}
                    