#!/usr/bin/env python
# coding: utf-8

# In[1]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
# zip 함수를 사용해 data 리스트값을 키값으로, close_price값을 value값으로 지정후, dict()함수를 사용해 새로운 딕셔너리를 생성함
close_table = dict(zip(date, close_price))
print(close_table)

