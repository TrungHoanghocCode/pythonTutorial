# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:58:51 2024

@author: Admin

21.Dictionary
"""

# giong 1 Object , ta co key : value
# dung {}, co the thay the value

hocSinh = {
    "hoTen" : "Nguyen A",
    "maLop" : "9a",
    "diemTB" : 8,
    }

print(hocSinh)

# lay phan tu

x = hocSinh["hoTen"]

print(x)
print(hocSinh["maLop"])

y = hocSinh.get("diemTB")

print(y)

# thay doi , them gia tri 

hocSinh["maLop"] = "10b"
hocSinh["monKem"] = "Anh"

hocSinh.update({"diemTB": 9.5, "monChuyen" : "Toan"})

print(hocSinh)

# xoa gia tri

# xoa theo key
hocSinh.pop("diemTB")

# xoa value cuoi cung , trc day popitem xoa ngau nhien 1 value 
hocSinh.popitem()

# xoa 1 muc hoac ca dic
del hocSinh["monKem"]
print(hocSinh)


# lay key hoac value
print(hocSinh.keys())
print(hocSinh.values())

for i in hocSinh.keys() :
    print(i)
for j in hocSinh.values() :
    print(j)
for m, n in hocSinh.items() :
    print(m , n)
# for k in hocSinh.items() :
#     print(k)


# lam` trong Dic
hocSinh.clear()
print(hocSinh) 