# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:34:42 2024

07.Comparison operators & Logic

@author: Admin
"""
#toan tu

x= int(input("nhap x: "))
y= int(input("nhap y: "))

print("{0}>{1} la {2}".format(x,y, x>y))
print("{0}<{1} la {2}".format(x,y, x<y))
print("{0}={1} la {2}".format(x,y, x==y))
print("{0}!={1} la {2}".format(x,y, x!=y))
print("{0}>={1} la {2}".format(x,y, x>=y))
print("{0}<={1} la {2}".format(x,y, x<=y))

#Logic 

z= int(input("nhap z: "))

print("{0}<{1} and {2}<{3} la {4}".format(x, y, y, z, x<y and y<z))
print("{0}<{1} or {2}<{3} la {4}".format(x, y, y, z, x<y or y<z))
print("not {0}<{1}  la {2}".format(x, y, not x<y))