# -*- coding: utf-8 -*-
"""
adv_p1_01.py
@author: III
"""
#Python 變數與名稱
a=2 #變數a指向整數物件(int object) 2
a   #顯示a所指向的物件內容 -->2
type(a) #a所指向的物件資料類型 (data type) #int
#------------------------------------------------------------
b=a #變數b指向變數a所指的物件
b   #顯示b所指向的物件內容 -->2
type(b) #b所指向的物件資料類型 (data type) #int
#------------------------------------------------------------
a='I Have a Apple' #變數a移情別戀,指向字串物件 'I Have a Apple'
a   #'I Have a Apple'
type(a) #str
#------------------------------------------------------------
#那麼,b有改變嗎?
b #2
type(b) #int
#------------------------------------------------------------
#猜猜看,如果b也移情別戀,會怎麼樣?
b=[2,4,6,8] #b指向一個list 物件 [2,4,6,8]