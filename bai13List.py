# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:47:31 2024]

13.List

@author: Admin
"""

# tao list rong
emptyList = []
# tao 1 doi tuowg list
emptyList02 = list()

print("List rong", emptyList,emptyList02)

#tao 1 List co du lieu

colors= ["red", "blue", "yellow","black", "gray"]

#lay tat ca
print("list ban dau")
print(colors)
print(colors[:])

#lay phan 
print("lay phan tu 0")
print(colors[0])

# lay phan tu co index tu x den y-1
print("lay 1 doan phan tu")
print(colors[1:3])

#them phan tu
#noi vao
colors.append("white")
print("sau khi append", colors)
#chen vao ngay index x 
colors.insert(1, "orange")
print("sau khi insert", colors)

#lay so luong phan tu
print("so luong phan tu: ", len(colors))

#thay doi gia tri mot phan tu
colors[0] = 'blue'
print("sau khi thay doi phan tu 0", colors)

#mot cach khac de append
colors[len(colors):]=["blue"]
print("Append kieu khac ne: ", colors)

#count phan tu voi dieu kien
print("Dem so phan tu blue: ", colors.count("blue")
)

#xoa mot phan tu 

#theo value
colors.remove("blue")
print("remove phan tu blue dau tien tu ben trai ", colors)
#cu phap remove phan tu co value tuong ung
# (check co thi xoa, ko thi thoi, ko bao loi)
if "blue" in colors:
    colors.remove("blue")
print("xoa blue neu co: ",colors)

#theo index
# del se xoa phan tu o index x,
del colors[0]
# pop se lay gia tri o index x di
removed_element  = colors.pop(0)
print("del index 0 la orange","va voi pop ta co duoc removed_element la: ",
removed_element,
".list co duoc la: ", colors)

#Dao nguoc List
colors.reverse()
print("sau khi dao nguoc",colors)

# Sap xep lai theo alphabet (neu la so thi tang dan)
colors.sort()
print("Sap xep lai theo alphabet: ",colors)

# Sap xep nguoc
colors.sort(reverse=True) 
print("Xep nguoc lai ne: ",colors)

# xoa sach du lieu 
colors.clear()
print("Xoa sach het ne: ", colors)