#!/usr/bin/env python
# coding: utf-8

# In[1]:


class OMG : 
    def print() :
        print("Oh my god")

>>> >>> myStock = OMG()
>>> myStock.print()
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given
    
#class OMG :
#    def print() :
#       print("Oh my god")
#
#
#mystock = OMG()
#mystock.print()      # OMG.print(mystock)
#
#omg클래스에 print함수를 정의했다. mystock클래스에서 print함수를 호출하면 다른 클래스에서 호출했으므로 계산인자값이 없어 함수가 실행되지 않는다.

