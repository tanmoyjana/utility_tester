"""it coverts the text file into a list"""
import re
def load(txt_file):
    final_list = []
    FILE = open(txt_file, 'r')
    raw_data = FILE.read()
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
    return final_list