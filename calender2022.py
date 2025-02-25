
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:53:08 2023

@author: masiyon
"""

import calendar as cal 
print (cal.calendar(2022))
def calc_volume( args): 
 vol=3.142* args [0]* args [0]* args[1] 
 print ("The volume is " + str(vol) + " cubed") 
 args[0]*=2 
 return 
dimensions=[7,10] 
print(dimensions) # before the function call 
calc_volume (dimensions) # first call to the function 
print(dimensions) # after the function call