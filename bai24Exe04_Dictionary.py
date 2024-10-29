# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 13:04:43 2024

@author: Admin

24.Ex04_Dictionary (Dic)
"""

# khai bao Dic
dicTest = {}


while (True) : 
    print(
        '''
        _____Menu____
        ___Pls pick:___
        1. Add 1 new world
        2. Search 1 world
        3. Update 1 world
        4. Del 1 world
        5. Del all world 
        6. Print all world 
        7. Print all
        8. End
        '''
        )
    
    # khai bao pick (user input)
    pick : int = int(input("Your choice ?: "))
    
    # add new / update
    if (pick == 1 or pick == 3):
        vocabulary : str = input("Add Vocabulary: ").strip().lower()
        mean : str = input("Add Mean: ").strip().lower()
        dicTest[vocabulary] = mean
        print("Added: ", vocabulary)
        
    # search
    elif (pick == 2):
        search : str = input("Search: ").strip().lower()
        print("Mean: ",search, ",", dicTest[search])
        
    # elif (pick === 3):
        
    # del
    elif (pick == 4):
        delete : str = input("Delete: ").strip().lower()
        a = dicTest.pop(delete) 
        print("Deleted: ", delete , a)
    
    # xoa all
    elif (pick == 5):
        dicTest.clear()
        print("All Clear !!!")
        
    # print all vocabulary
    elif (pick == 6):
        print("List vocabulary")
        for x in dicTest.keys() :
            print(x)
            
    # print all
    elif (pick == 7):
        print(" Full List")
        for x, y in dicTest.items() :
            print(x , y)
    
    # 8 thi break ket thuc vong
    elif (pick == 8):
        print("Thanks !!!!!!")
        break
    else : 
        print("Pls check your choice ! it should be a num 1~8")
        
    # con thieu phan serach ko co tu , bo sung sau 
    
        