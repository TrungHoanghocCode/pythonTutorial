# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:08:52 2024

@author: Admin

19.Break & continue
"""

# Break
# i=0
for i in range(1,10):
    print(i)
    if (i>=5):
        break

n = 100
while (n>0) :
    n=n//2
    if(n<=10):
        break
    print(n)

# break se break vong gan nhat, khong break het code
for x in range (1,10):
    for y in range (2,10):
        print("{0}*{1}={2}".format(x,y,x*y))
        if (y >= 5) : 
            break
    print("\n")
    
    
# continue se bo qua 1 dieu kien nao do trong khi loop

for z in range (1,10):
    if (z % 2 == 1 ):
        continue
    print(z)