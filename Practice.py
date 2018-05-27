## -*- coding: utf-8 -*-
#"""
#Created on Tue Feb 13 15:11:56 2018
#
#@author: julius
#"""
#import functs
#
#def find_10(array10):
#    for i, n in enumerate(array10):
#        try:
#            array10.index(10 - n)
#            if i != array10.index(10-n):
#                return True
#            continue
#        except:
#            continue
#    return False
#    
##print find_10([1, 2, 3, 4, -4])
#
#def longest(string):
#    longest = ""
#    word = []
#    for i, c in enumerate(string):
#        if c.isalpha() or c.isdigit():
#            word.append(c)
#            if i == (len(string) - 1):
#                if len(word) > len(longest):
#                    longest = "".join(word)
#        else:
#            if len(word) > len(longest):
#                longest = "".join(word)
#            del word[:]
#    return longest
#    
#def longest2(string):
#    workString = string.split()
#    currLong = ""
#    for i, w in enumerate(workString):
#        if len(w) > len(currLong):
#            currLong = w
#    return currLong
##print longest("the cat in the hat was the gayest of the bunch123")
##print longest2("the cat in the hat was the gayest of the bunch123")
#    
#def phi(num):
#    num0 = 1
#    num1 = 1
#    for i in range(0, num):
#        num0, num1 = num1, num0 + num1
#    return float(float(num1)/float(num0))
##print phi(1200)
#def dick(length):
#    dickString = ["8"]
#    for i in range(0, length):
#        dickString.append("=")
#    dickString.append("D")
#    return "".join(dickString)
##print dick(10000)
#
###### return true if a letter or number repeats 5 or more times in a string
###### also return the letters, and number of times it repeats
#def rep5(string):
#    count = 1
#    retArray = []
#    for i, c in enumerate(string):
#        if c.isalpha() or c.isdigit():
#            try:
#                retArray.index(c)
#                continue
#            except:
#                pass
#            for c2 in string[i + 1:]:
#                if c == c2:
#                    count = count + 1
#            if count > 4:
#                retArray.append(c)
#                retArray.append(count)
#            count = 1
#        
#    return retArray
##data = rep5("asasdf1234adfasdjknvoxicjv3b1ir4baodhfbasnfnajhrb0123urbkjasdbfg0pqwbrojqwber01u23bqijnwdbfadbfgoq2j3br0123br")
#
#def properPrint(rep):
#    check = False
#    for i in range(0, len(rep)):
#        if check == False:
#            print (rep[i] + " is repeated " + str(rep[i + 1]) + " times!")
#            check = True
#        else:
#            check = False
#        
##properPrint(data)
#        
#stock_prices_yesterday = [7, 7, 5, 3, 11, 23, 33, 16, 44, 52]
#
#test = functs.functions()
#stuff = test.stocks(stock_prices_yesterday)




#def MaximalSquare(strArr): 
#    #### POPULATE A CHECK ARRAY
#    checkArray = []
#    pop = []
#    subArray = []
#    #### FIRST CHECK DIMENSION OF ARRAY
#    rows = len(strArr)
#    columns = len(strArr[0])
#    if rows > columns:
#        minSubSize = columns
#    elif rows < columns:
#        minSubSize = rows
#    else:
#        minSubSize = columns
#    x = 0
#    y = 0
#    SubSize = minSubSize
#    while SubSize > 1:
#        ### GENERATE SUB MATRIX ###
#        for i in range(y, y + SubSize):
#            subArray.append(strArr[i][x : x+SubSize])
#        ### GENERATE CHECK MATRIX ###
#        for i in range(0, SubSize):
#            pop.append('1')
#        for i in range(0, SubSize):
#            checkArray.append("".join(pop))
#        ### CHECK FOR MATCH ###
#        print "This is a SUB"
#        print subArray
#        print "this is a CHECK"
#        print checkArray
#        print "###############"
#        if checkArray == subArray:
#            return len(checkArray)**2
#        ### IF NOT MATCH DELETE AND MOVE OVER ###
#        del subArray[:]
#        del checkArray[:]
#        del pop[:]
#        x = x + 1
#        if x + SubSize <= columns:
#            continue
#        elif x + SubSize > columns:
#            x = 0
#            y = y + 1
#            if y + SubSize <= rows:
#                continue
#            elif y + SubSize > rows:
#                x = 0
#                y = 0
#                print ("here")
#                SubSize = SubSize - 1
#    return 1
#    
## keep this function call here
#test = ["1110","0111","1011","1011"]
#print MaximalSquare(test)  


