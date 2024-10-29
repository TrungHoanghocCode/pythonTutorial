# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:22:51 2024

@author: Admin

14.Loop FOR
"""

# =============================================================================
# x : int = int(input("Nhap x: "))
# total  : int = 0
# for i in range(x+1):
#     # print(x)
#     total += i
# print(total)
# =============================================================================

# x trong ham range phai la so nguyen
# for [bien index] in range[dieu kien chay loop]:
    # thuc thi 

# =============================================================================
# x : float = float(input("Nhap x: "))
# total  : float = 0.0
# for i in range(int(x)+1):
#     # print(x)
#     total += i
# print(total)
# =============================================================================

# Range (index start, index limit, buoc nhay)

# =============================================================================
# y : int = 20
# for i in range(6, y, 3):
#     print(i)
# =============================================================================


colors = ["red", "blue", "green", "black", "white", "brown"]

for color in colors :
    print (color)
print("END")
for i in range (1,len(colors),2):
    print(colors[i])