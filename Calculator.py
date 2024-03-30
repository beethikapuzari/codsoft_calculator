#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num1=float(input("enter 1st no here:"))
num2=float(input("enter 2nd no here:"))
print("press 1 for addition\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division")
choice=int(input("enter your choice from 1-4:"))
if choice== 1:
    print("The addition of given two no is",  num1+num2)
elif choice== 2:
    print("The subtraction of given two no is", num1-num2)
elif choice== 3:
    print("The multiplication of given two no is", num1*num2)
elif choice== 4:
    print("The division of given two no is", num1/num2)
else:
    print("invalid input")

