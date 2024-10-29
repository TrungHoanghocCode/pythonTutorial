# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:56:41 2024

@author: Admin

26.lambda
"""

kiemTraSoChan = lambda a : (a%2==0)
b = kiemTraSoChan(5)
print(b)

# khai bao hamMu la 1 function
def hamMu (n) : 
    # tra gia tri la 1 ham lambda
    return lambda x : x**n

# khai bao ham con
# Gán hamMu2 = hamMU(2) như 1 cách khai báo 1 hàm lambda 
#hamMu2 = lambda x : x**2
hamMu2 = hamMu(2)
hamMu3 = hamMu(3)
hamMu4 = hamMu(4)


# lay gia tri

print(hamMu2(6))
z = hamMu4(9)
print(z + 1)