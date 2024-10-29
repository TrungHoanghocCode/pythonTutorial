# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:48:58 2024

@author: Admin

15. Loop in loop
"""

#  in bang cuu chuong 2

# for i in range(0,11,1):
#     print ("{0}*2={1}".format(i,i*2))
    
    
# thu in nhieu bang cuu chuong
    
for j in range (2 , 5 , 1):
    print("Bang cuu chuong: ", j)
    for i in range(1,11,1):
        print ("{0}*{1}={2}".format(i,j,i*j))