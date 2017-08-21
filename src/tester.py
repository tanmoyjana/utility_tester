from sys import argv
import os.path
import imp
import re
script, sig, py_file = argv
table = {'ChristmasTreeDecoration.solve' : ['py1-ChristmasTreeDecoration.sol.txt', 10], 
         'NonCoprimeGraph.distance' : ['py1-NonCoprimeGraph.sol.txt', 10], 
         'MealPlan.countDistinct' : ['py1-MealPlan.sol.txt', 10],
         'RandomPancakeStack.expectedDeliciousness' : ['py1-RandomPancakeStack.sol.txt', 10], 
         'AdditionGame.getMaximumPoints' : ['py1-AdditionGame.sol.txt', 10], 
         'ATaleOfThreeCities.connect' : ['py2-ATaleOfThreeCities.sol.txt', 10], 
         'CrossWord.countWords' : ['', 10], 
         'IntoTheMatrix.takePills' : ['', 10], 
         'EventOrder.getCount' : ['', 10], 
         'Abacus.add' : ['', 10],
         'AccountBalance.processTransactions' : ['', 10],
         'WordFind.findWords' : ['', 10], 
         'OddEvenTree.getTree' : ['py1-OddEvenTree.sol.txt', 10], 
         'RepeatedSubstrings.decompress' : ['py1-RepeatedSubstrings.sol.txt', 10]}
DATA_DIR = 'data'

def load(txt_file):
    final_list = []
    f = open(txt_file, 'r')
    raw_data = f.read()
    p1 = ('System Test Results')
    p2 = ('Passed')
    txt_data = raw_data[raw_data.find(p1) +len(p1)+ 1 : raw_data.rfind(p2)+ len(p2)].strip()
    final_data1 = re.sub('\n+', '\n', re.sub('\t+', '\t', txt_data))
    final_data = final_data1.replace('{', '[').replace('}', ']')
    list_str = final_data.split('\n')
    for item in list_str:
        value = item.strip().split('\t')
        final_list.append([value[0], value[1]])
    final_list.pop(0)
    x = os.path.join(DATA_DIR, table[sig][0].split('.txt')[0] + '.test.dat')
    output = open(x, 'w')
    output.write(str(final_list))
    output.close
    return final_list

x = os.path.join(DATA_DIR, table[sig][0])
ls = load(x)    

def tester(signature, file_name):
    result = []
    sig1 = str(signature).split('.')
    sig2 = sig1[0] + '().' + sig1[1]
    try:
        f1 = imp.load_source(sig2, file_name)
        for value in ls:
            signature1 = 'f1.' + sig2 +'(' + value[0] + ')'
            try:
                x = eval(signature1) 
                y = eval(value[1])
                if  x == y:
                    result.append('passed')
                else:
                    result.append('failed')
            except:
                result.append('Error')
    except IOError:
        return 'There is no such file or directory: %r' % py_file
    d = {'total' : len(ls), 'pass' : result.count('passed'), 'fail' : result.count('failed'), 'error' : result.count('Error')}
    path = os.path.join('result_output', py_file[py_file.find("submission")+ len('submission')+ 1 : py_file.rfind('.py')+ len('.py')]+ '.test.output.dat')
    output = open(path, 'w')
    output.write(str(d))
    return d
     
	
if __name__ == "__main__":
   print tester(sig, py_file)
