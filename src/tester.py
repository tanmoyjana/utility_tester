from sys import argv
import os.path
import imp
import re
from table import TABLE
from convert import load
script, sig, py_file = argv

DATA_DIR = 'data'
def tester(signature, file_name):
    try:
        FILE_NAME = TABLE[sig][0].split('.txt')[0] + '.test.dat'
        PATH = os.path.join('data_sol', FILE_NAME)
        path = os.path.join(DATA_DIR, TABLE[sig][0])
        if os.path.isfile(PATH) == True:
            ls = open(PATH, 'r').read()
        else:
            output = open(PATH, 'w')
            output.write(str(load(path)))
            output.close
            ls = open(PATH, 'r').read()
    except KeyError:
        return 'There is no such signature %r' % sig
    try:
        LS = eval(ls.strip())
    except SyntaxError:
        LS = load(path)
    result = []
    fail = []
    error = []
    pas = []
    sig1 = str(signature).split('.')
    sig2 = sig1[0] + '().' + sig1[1]
    try:
        f1 = imp.load_source(sig2, file_name)
    except IOError:
        return 'There is no such file or directory: %r' % py_file
    for value in LS:
        signature1 = 'f1.' + sig2 +'(' + value[0] + ')'
        try:
            x = eval(signature1) 
            y = eval(value[1])
            if x == y:
                result.append('passed')
                pas.append(value[0])
            else:
                result.append('failed')
                fail.append(value[0])
        except SyntaxError:
            result.append('Error')
    d = {'total' : len(LS), 'pass' : result.count('passed'), 
         'fail' : result.count('failed'), 'error' : result.count('Error')}
    #path = os.path.join('result_output', py_file[py_file.find("submission")+ 
#len('submission')+ 1 : py_file.rfind('.py')+ len('.py')]+ '.test.output.dat')
    #output = open(path, 'w')
    #output.write(str(d))
    return d

     
	
if __name__ == "__main__":
    print tester(sig, py_file)
