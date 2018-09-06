""" Cryptanalysis.py

    A command-line tool implimenting simple ciphers and
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
    
    Copyright 2018, Daiya Masuda
"""



import os
import sys

class Distribution(object):
    """ Base class for analysis routines for symbol distributions.
        Results are dictionary objects with human readable keys.
    """
    def to_readable(self):
        """ Convert dictionary of symbols to readable text """
        pp = []
        print self.result
        for nary in self.result:
            pp.append( "{}: {}\n".format( nary, self.result[nary]))
        return ''.join(pp)

class Ngraph(Distribution):
    """ Looking 'n' symbols at a time, create a dictionary
        of the occurrences of the n-ary string of symbols.
        Default is n=1, a monograph.
    """
    def __init__(self, n=1 ):
        self.n = n

    def analyze(self, text):
        n = self.n
        self.result = {} # results are stored as a dictionary
        for i in range( len(text) - n - 1 ):
            nary = text[ i:i+n ]
            if nary in self.result:
                self.result[nary] += 1
            else:
                self.result[nary] = 1
        return self.result

class Bruteforce(Distribution):
    """
    Bruteforce using shifting alphabets one by one. 
    Will output every possible combinations (26 shifts) into a text file. 
    """
    def analyze(self,text):
        self.result = Brute().analyze(text)

class Brute(Distribution):

    def analyze(self,text):
        self.result = {}
        temp = []
        translated = translateNum(text)
        print text
        for i in range (26):
            for j in range(0,len(text)-1):
                nary = translated[j]
                if(nary is not ' '):
                    nary = int(nary)+ i
                if(nary > 26):
                    nary = 1
                temp.insert(j,nary)
            print temp
            converted = ''.join(str(v) for v in temp)
            self.result[i] = translateStr(converted)
        return self.result

        self.result = {}
table = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "o":15,
        "p":16,
        "q":17,
        "r":18,
        "s":19,
        "t":20,
        "u":21,
        "v":22,
        "w":23,
        "x":24,
        "y":25,
        "z":26,
        " ":" "
    }
res = {
    "1":"a",
    "2":"b",
    "3":"c",
    "4":"d",
    "5":"e",
    "6":"f",
    "7":"g",
    "8":"h",
    "9":"i",
    "10":"j",
    "11":"k",
    "12":"l",
    "13":"m",
    "14":"n",
    "15":"o",
    "16":"p",
    "17":"q",
    "18":"r",
    "19":"s",
    "20":"t",
    "21":"u",
    "22":"v",
    "23":"w",
    "24":"x",
    "25":"y",
    "26":"z",
    " ":" "
    }

def translateNum(text):
    translated = []
    for i in range (len(text) - 1):
        nary = text[i:i+1]
        translated.insert(i,table[nary])
    return translated

def translateStr(text):
    translated = []
    for i in range (len(text)-1):
        nary = text[i:i+1]
        print nary
        translated.insert(i,res.get(nary))
    return translated

class Monograph(Distribution):
    def analyze(self, text): 
        self.result = Ngraph( n = 1 ).analyze(text)

class Digraph(Distribution):
    def analyze(self, text): 
        self.result = Ngraph( n = 2 ).analyze(text)

class Trigraph(Distribution):
    def analyze(self, text): 
        self.result = Ngraph( n = 3 ).analyze(text)

class Skipgraph(Distribution):

    """
    Skipgraph ((https://en.wikipedia.org/wiki/N-gram#Skip-gram))

    """
    def analyze(self, text):
        self.result = Skip().analyze(text)

class Skip(Distribution):
    def analyze(self,text):
        self.result = {}
        splitSpace = text.split(" ")
        for i in range ( len(splitSpace) - 2 ):
            nary = splitSpace[i] + " " + splitSpace[i+2]
            if nary in self.result:
                self.result[nary] += 1
            else:
                self.result[nary] = 1
        return self.result

            
            
# collect all distribution routines for cli usage
dist_dict = {'mono':Monograph, 'di':Digraph, 'tri':Trigraph, 'ng':Ngraph, 'sk':Skipgraph, 'br':Bruteforce}
dist_name_list =[ key for key in dist_dict]

def Dist(dist_name, input_file, output_file):
    """ Calculate frequency distributions of symbols in files."""

    D = dist_dict[dist_name] # instantiate class from dictionary
    dist = D()
    text = input_file.read()

    dist.analyze(text)

    print( dist.to_readable() )


def locateFile(filename):

    """
    A method to locate txt file
    """
    if(".txt" not in filename):
        filename = filename + ".txt"

    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    if(filename not in files):
        return False

    return True


if __name__ == "__main__":

    active = True
    print("Please enter the name of text file you want to analyze: \n")
    filename = raw_input()


    if(locateFile(filename) == False):
        while locateFile(filename) == False:
            print("Error! File not found. Make sure it is in the same folder as this program. \n")
            print("Please re-enter the name of text file you want to decrypt: \n")
            filename = raw_input()
            locateFile(filename)

    print("Please enter the name for the output file.")
    output_name = raw_input()
    file = open(filename)
    output_file = open(output_name,"w+")

    cipher_text = file.read()

    while(active == True):
        print("Which would you like to do?: \n")
        #'mono':Monograph, 'di':Digraph, 'tri':Trigraph, 'ng':Ngraph
        print("For Monograph type 'mono', For Digraph type 'di', \n")
        print("For Trigraph, type 'tri', For Ngraph type 'ng'. \n")
        print("For Skipgraph, type 'sk'. For Brute Forcer type 'br' \n")
        dist_name = raw_input()

        D = dist_dict[dist_name] # instantiate class from dictionary
        dist = D()

        dist.analyze(cipher_text)

        output_file.write( dist.to_readable() )

        print("Done! Check output file \n")
        print("Type q if you want to quit, otherwise press enter \n")
        last = raw_input()
        if last is 'q':
            active == False
            sys.exit()




