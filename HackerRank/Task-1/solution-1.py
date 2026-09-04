#!/bin/python3

import math
import os
import random
import re
import sys

# practice if-else

if __name__ == '__main__':
    n = int(input().strip())

        
if n % 2 != 0:
    print("Weird")
    
elif  2 <= n <= 5: # could also be elif n in range(2,6): 
    print("Not Weird")
    
elif 6 <= n <= 20: # could also be elif n in range(6,21):
    print("Weird")
    
elif n > 20:
    print("Not Weird")          
        