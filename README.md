Cryptanalysis.py

    This is a command-line tool implimenting simple ciphers and
    basic frequency analysis tools.
    
    Usage: python Cryptanalysis.py... and follow the instructions in CLI.
    
    Commands:
       'mono':Monograph analysis
       'di':Digraph analysis
       'tri':Trigraph analysis
       'ng':Ngraph analysis
       'sk':Skipgraph analysis
       
       'br':Bruteforce decipher ##WORK IN PROGRESS (NOT WORKING)         
        
    Example usage:
    
    $./Cryptanalysis.py 
    $./test.txt ((INPUT FILE))
    $./temp     ((OUTPUT FILE))
    $./mono ((MONOGRAPH ANALYSIS))
    $./di ((DIAGRAPH ANALYSIS))
    $./q ((Q TO QUIT))
    
Bruteforce decipher is still in works. Currently broken.
This program was written with Python 2.7.
os and sys are used to make sure the input file exists. 

Reference for Skipgram (https://en.wikipedia.org/wiki/N-gram#Skip-gram)

Copyright 2018, Daiya Masuda