# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:49:24 2024

12.Exe 01

@author: Admin
"""
import math
# Giai phuong trinh bac 2 ax2 + bx + c = 0

#Nhap lieu 

print("Giai ptr bac II ax2 + bx + c = 0")

a = float(input("Add a: "))

b = float(input("Add b: "))

c = float(input("Add c: "))

print("Giai ptr bac II: {0}x2 = {1}x + {2} =0".format(a, b,c))

#Xu li

if (a!=0) :
    delta = b**2 - 4*a*c
    if(delta < 0):
        print("Ptr vo nghiem")
    elif(delta==0):
        x=-b/2*a
        print('Co nghiem kep x= ', x)
    else:
        x1 = (-b-math.sqrt(delta)) / (2*a)
        x2 = (-b+math.sqrt(delta)) / (2*a)
        print("Ptr co 2 nghiem x1={} va x2={}".format(x1, x2))
else :
    print("a =0 => Khong con la ptr bac II")