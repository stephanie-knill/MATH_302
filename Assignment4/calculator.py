# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:34:46 2016

@author: Stephanie
"""

#from scipy.special import comb
#from math import log
import math


#Question 3

n=537
p = 1/576
l =n*p

k=0
p_0 = math.exp(-l)*l**k/math.factorial(k)
e_0 = p_0 * n

k=1
p_1 = math.exp(-l)*l**k/math.factorial(k)
e_1 = p_1 * n

k=2
p_2 = math.exp(-l)*l**k/math.factorial(k)
e_2 = p_2 * n

k=3
p_3 = math.exp(-l)*l**k/math.factorial(k)
e_3 = p_3 * n

k=4
p_4 = math.exp(-l)*l**k/math.factorial(k)
e_4 = p_4 * n

#k >5
p_g5 = 1 - p_0 - p_1 - p_2 - p_3 - p_4
e_g5 = p_g5 * n


# Check : sum p_i = 1
sum = p_0 + p_1 + p_2 + p_3 + p_4 + p_g5
