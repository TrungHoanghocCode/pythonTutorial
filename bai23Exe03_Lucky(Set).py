# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:03:14 2024

@author: Admin

23.Exe03_Lucky (SET)
"""

# =============================================================================
# Tao 1 ung dung them, xoa, quay 1 so ngau nhien trung thuong 
# =============================================================================

import random
# khai bao box
box : set = set()
a= True
while (a) : 
    print(
      '''
      _____Menu____
      ___Pls pick:___
      1. Add 1 number xxx
      2. Del 1 number xxx
      3. Random 1 Lucky_number 
      '''
      ),
    print("Now: ",box )
    
# khai bao pick
    pick : int = int(input("Pls pick 1/2 or 3: "))

# xu li 

    if pick == 1 :
        num : int = int(input(" You want to add (xxx): "))
        box.add(num)
    elif pick == 2: 
        num : int = int(input(" You want to remove (xxx): "))
        box.discard(num)
    elif pick == 3:
        if (len(box) > 0 ):
            x =  random.choice(list(box))
            print("Lucky number is: ", x)
            box.discard(x) 
        else:
            print("Box is empty, can not choose 3")
        a = False     
    else:
        print("Pls check Your choose !!! ***************" )
    
