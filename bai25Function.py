# # -*- coding: utf-8 -*-
# """
# Created on Sat Jun 15 10:30:34 2024

# @author: Admin

# 25.Function
# """

# # khai bao 1 func

# def hamCoBan ():
#     print("hello W !")
    
# # goi func
# hamCoBan()

# # agrument
# ho: str = "Hoang"
# ten : str = "Trung" 
# def hamDoiSo (ho , ten):
#     print("Hello ", ten, ho)
# hamDoiSo(ho, ten)

# # khi chua xac dinh duoc bao nhieu doi so, xac dinh thong qua index : *
# def thoiKhoaBieu (*monHoc) :
#     # for x in monHoc:
#         print(monHoc[1], monHoc[0], monHoc[2])
        
# thoiKhoaBieu("Toan", " Li", "hOA")

# def total (*value):
#     sum = 0 
#     for y in value:
#         sum += y
#     print(sum)
# total(3,5,6,9)

# # truyen nhieu doi so, xac dinh thong qua key : **
# def xinChao(**hoVaten):
#     print("Hello:" , hoVaten["ten"])
# xinChao(ho = "Hoang", lot = "Dinh", ten = "Trung")


# # dung return de lay gia tri

# def phepNhan (*value) :
#     result : int = 1
#     for z in value:
#         result *= z
#     # voi return thi ham se ngung lai
#     return result
# abc = phepNhan(2,2,2,2,2)
# print(abc + 1)
    

# # Ex USCLN
# a = int(input("Nhap a: "))
# b = int(input("Nhap b: "))

# def gcd (a,b):
#     while(a != b):
#         if a> b :
#             a -= b
#         else:
#             b -= a
#     return a

# uscln = gcd (a, b)
# print("USCLN cua a, b la: ", uscln)


# Ex tinh tong

listNum = []
if (len(listNum) <= 3):
    for i in range(3):
        n = int(input("Nhap n: "))
        listNum.append(n)
        
print(listNum)
def tinhTong (listNum) : 
    for x in listNum:
        total = 0 
        total = total + x
        print(total)
    return total

abc = tinhTong(listNum)
print(abc)


# ex1 : nhap 1 day so nguyen, cho biet so luong so chan so le
#  ex 2 : nhap 1 day so , tra ve 1 day so da sap xep 
