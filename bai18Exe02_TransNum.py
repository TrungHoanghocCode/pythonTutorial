# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:20:01 2024

@author: Admin

18.Thap phan sang nhi phan
"""

#  Nhap x bat ki va chuyen no sang he nhi phan 

# nhap x > 0
x = -1 
while (x<=0):
    x = int(input("Nhap x: "))
    
# trans

result = ""

while (x > 0) : 
    # xet x > 0 thi x/2 lay so du chen vao result 5/2 du 1 => result = 1
    # tiep tuc 5/2 = 2 , 2/2  du 0 => result = 01 ..... 
    result = str(x%2) + result
    # chia 2 lay phan nguyen 5/2 = 2
    x = x//2
print("Result: ", result)