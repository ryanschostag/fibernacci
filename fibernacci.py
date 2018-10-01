#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:31:59 2018

@author: Ryan Schostag

https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence
Answer by Aaron Hall for function F(n, _cache{})

Fibernacci numbers are commonly used. For example, SCRUM poker for ranking 
task difficulty

Accepts command line arguments and prints a table of n and F(n) up to the value provided. 
Value provided is a max value where the algorithm stops. For example:
    
    python3.5 fibernacci.py 9.2 10 2000 hello 15
    
    ###############
    #1: F(9.2)
    ###############
    
    n	F(n)
    
    0	0
    1	1
    2	1
    3	2
    4	3
    5	5
    6	8
    
    
    ###############
    #2: F(10)
    ###############
    
    n	F(n)
    
    0	0
    1	1
    2	1
    3	2
    4	3
    5	5
    6	8
    
    
    ###############
    #3: F(2000)
    ###############
    
    n	F(n)
    
    0	0
    1	1
    2	1
    3	2
    4	3
    5	5
    6	8
    7	13
    8	21
    9	34
    10	55
    11	89
    12	144
    13	233
    14	377
    15	610
    16	987
    17	1597
    
    
    ###############
    #4: F(hello)
    ###############
    
    "hello" is not a numeric type
    
    ###############
    #5: F(15)
    ###############
    
    n	F(n)
    
    0	0
    1	1
    2	1
    3	2
    4	3
    5	5
    6	8
    7	13
    

You can write the data to a file by using `python fibernacci.py 10 > file.txt`.

You may also import fibernacci.py as a module to use F(n, _F={}) your way. 

"""

from sys import argv

def F(n, _F={}):
    """ 
    Efficiently memorized recursive function, returns a Fibernacci number
    :param: n: <int> a starting point value
    :return: fibernacci value of n
    """
    # check the cache and return _F[n] if found in cache
    if n in _F:
        return _F[n]
    # evaluate F(n) = F(n-1) + F(n-2)
    elif n > 1:
        return _F.setdefault(n, F(n-1) + F(n-2))
    # return n if n == 0
    return n


def main(*args):
    
    sym = '#'
    
    if len(args) == 0:
        print('No fibernacci numbers were supplied. Try again')
        return 0
    
    for arg_n, arg in enumerate(argv):
        
        statement = '#{}: F({})'.format(arg_n, arg)
        sym_n = len(statement) if len(statement) > 15 else 15
        
        if arg_n == 0:
            continue
        
        print(sym*sym_n)
        print(statement)
        print(sym*sym_n)
        
        # Evaluate float vs integer to round float and convert to int
        
        try:
            
            arg_f = float(arg)
            arg_i = int(float(arg))
            
            if arg_f != arg_i:
                arg = round(arg_f) // 1
            else:
                arg = arg_i
                
        except ValueError as val_err:
            print('\n"{}" is not a numeric type\n'.format(arg))
            continue
                
        max_n = arg
            
            
        
        print('\n{}\t{}\n'.format('n', 'F(n)'))
        
        for n in range(max_n):
            
            if F(n) >= max_n:
                break
            
            print('{}\t{}'.format(n, F(n)))
        
        print('\n')
    

if __name__ == "__main__":
    main(argv)
