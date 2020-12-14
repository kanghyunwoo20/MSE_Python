#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 논리 연산자 or을 사용해서 두 개의 확장자를 비교합니다.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(변수)

