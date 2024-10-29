# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:31:23 2024

@author: Admin

19.Tuple
"""

# chuoi cac phan tu co index ( giong list) nhung gia tri la cac hang so
# dung () , co the lap gia tri 


gioiTinh = ("Nam", 'Nu')
manga = ("Conan", "Doraemon", "Gintama", "OP", "Gintama", "Gintama")
lopHoc = (1,2,3,4,5,6,7,8,9,10,11,12)


print(manga[0])
print(manga[0:3])

# =============================================================================
# #  err neu thay doi gia tri
# manga[0] = "Yaiba"
# 
# =============================================================================


for x in gioiTinh : 
    print(x)
    
#  cong tuple

y = manga + gioiTinh
print(y)

# nhan tuple

z = gioiTinh *2 
# v = gioiTinh * manga    ko nhan 2 tuple dc 
print(z)

# in
print ("OP co trong manga khong: ", "OP" in manga)
print ("OPM co trong manga khong: ", "OPM" in manga)

# len
print("so phan tu cua manga: ",len(manga))

# count
print("so phan tu Gintama: ",manga.count("Gintama"))

# min max (neu la str thi theo alphabet)
print("Max cua manga: ", max(manga) )
print("Min cua manga: ", min(manga) )

# Sum chi dung cho tuple full int
print("Sum cua lopHoc: ", sum(lopHoc))

# sort sap xep lai tuple va CHUYEN NO THANH LIST
listManga = sorted(manga)
print(listManga)
