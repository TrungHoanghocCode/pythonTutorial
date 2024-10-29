# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 21:37:20 2024

@author: Admin

16.String
"""

# cong chuoi

s1 = "hello"
s2 = " world !!!"
s3 = s1 + s2 
print(s3)

# chuoi nhieu dong

s4 = """
alo 
tao 
la 
teo
"""

print(s4)

# \n va str co the nhan

s5 = " Ngay mai troi se sang ! \n"
s6 = s5*5
print(s6)

# Kiem tra chuoi con

s7 = "500*100"
s8 = "*"
s9 = "/"

if s8 in s7 :
    print(500*100)
else: 
    print("s8 ko co trong s7")
    
    
#  Viet hoa

s10 = "song sau tinh lang \nlua chin cui dau \nsong oi la song"

#  ki tu dau cua chuoi 
s11 = s10.capitalize()
# co the  viet la s11 = str.capitalize(s10)
print(s11)

# viet hoa toan bo 
s12 = s10.upper()
print(s12)

# viet thuong toan bo
s13 = s12.lower()
print(s13)

# find  
s14 = s10.find("song")
s15 = s10.find("nui")
print(s14,s15)
# tra -1 neu ko co , tra ra index neu co (find)

# count
s16 = s10.count("song")
print(s16)

# replace
s17 = s10.replace("song", "SONG", 2)
print(s17)

# cat str thanh list
lists18 = s10.split(" ")
print(lists18)

# lay chuoi con
s19 = s10[18:38]
print(s19)