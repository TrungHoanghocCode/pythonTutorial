# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:44:02 2024

@author: Admin

11.IF & Else
"""

x = int(input('Nhap x vo de: '))

# if

if (x >  0) :
    print(" x la so duong ")
    
    
# if else 

if (x%2 == 1) :
    print(" x khong chia het cho 2 ")
    
else :
        print ("x chia het cho 2 ")
    
    

#  if else if else 

if x >= 8 :
    print(x, "diem : du gioi")
elif x >= 6 :
    print(x, "diem : kha nhen")
elif x>= 5 :
    print (x, "diem: trung binh")
else:
    print("thang lz nay lam sao the!?")


print("end!!!")