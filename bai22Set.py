# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:09:28 2024

@author: Admin

22.Set
"""

# cac phan tu của SET ko co thu tu (index),  ko duoc trung nhau, ko the thay doi
# co the xoa , them phan tu
# dung {}

monHoc = {"Toan", "Li", "Hoa",}
print(monHoc)

# duyet phan tu
for x in monHoc :
    print(x)

# + phan tu
monHoc.add("Anh")
print(monHoc)    
# ke ca co them 1 lan nua cung chi co 1 "Anh"
monHoc.add("Anh")
print(monHoc)    

# + 1 set 
hocThem = {"Hat","Dan",}
monHoc.update(hocThem)
print(monHoc)

# + 1 List (phan tu trung nhau trong list chi con 1)
hocGioi = ["Ve", "Sinh", "Su", "Su"]
monHoc.update(hocGioi)
print(monHoc)

# xoa phan tu

# remove se bao loi neu ko co phan tu de xoa 
# monHoc.remove("Dia")

# discard co thi xoa ko thi thoi (chi dc xoa 1 )
monHoc.discard("Anh")
monHoc.discard("Dia")
print(monHoc)

# pop lay di phan tu dau tien
z = monHoc.pop()
print(z)
print(monHoc)

# clear lam rong set
monHoc.clear()
print(monHoc)

# del xoa luon ca bien 
del monHoc
# print(monHoc)

