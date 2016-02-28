# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:34:46 2016

@author: Stephanie
"""

from scipy.special import comb
import math
from math import log
 
# Question 2

n=7
sum = 0
for k in range(4,7+1):
    c = comb(n,k, exact=False)
    Y = c * (.6**k)*(.4**(n-k))
    sum += Y
    
    
    
    
## P(Y =4)
#k=4
#c = comb(n,k, exact=False)
#y4 = c * (.6**k)*(.4**(n-k))
# 
## P(Y=5)
#k=5
#c = comb(n,k, exact=False)
#y5 = c * (.6**k)*(.4**(n-k))
#
## P(Y=6)
#k=6
#c = comb(n,k, exact=False)
#y6 = c * (.6**k)*(.4**(n-k))
#
## P(Y=7)
#k=7
#c = comb(n,k, exact=False)
#y7 = c * (.6**k)*(.4**(n-k))
#
## Sum
#y = y4+y5+y6+y7


    

# Question 6: Section 5.1 #14

# Part a)
n=10000
k=0
p = 1/1000
q = 1- p
c = comb(n,k, exact=False)
P_none = c* (q)**n

# Part b)
num_ppl = log(1/2) / math.log(q)
