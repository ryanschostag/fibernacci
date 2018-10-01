# fibernacci

Author: Ryan Schostag

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
