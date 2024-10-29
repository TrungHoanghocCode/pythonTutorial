# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:29:46 2024

@author: Admin

17.While
"""

# vong lap while thuong dung khi khong biet nen lap bao nhiu lan


# Yeu cau nhap x, neu x<=0 thi nhap lai cho den khi nao dung 
x = -9
while (x<=0) :
    x = int(input("Nhap x: "))
    
    
# doi voi trg hop biet truoc lap bao nhieu lan

# Tinh tong tu 0 den x 
total = 0 
# =============================================================================
# for i in range (x+1) :
#     total += i
# print(total)
# =============================================================================

i = 0
while (i<=x) :
    total += i
    i += 1
print("total = ", total)

#  else

j = 0 
while (j<=x):
    print(j, "j - be hon x")
    j += 1
else:
    print(j,"j - lon hon x roi")


# break

z = 0 
while (z<=x):
    print(z, " z - be hon x")
    z += 1
    if (z>=3):
        break
else:
    print(z,"z - lon hon x roi")
    
