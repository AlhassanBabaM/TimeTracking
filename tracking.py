#!/usr/bin/env python
# coding: utf-8

# In[2]:



nana = input('employee:')
hworked = int(input('Please enter the hours worked:'))
hwage = int(input('Please enter the hourly wage:'))
if hworked>3:
  print('The gross pay is',(hworked - 0.5 ) * (hwage) * 5 + (hwage * (hworked - (hworked - 0.5))),'$')
else:
  print('The gross pay of the worker is', hworked * hwage, '$')


# In[ ]:




