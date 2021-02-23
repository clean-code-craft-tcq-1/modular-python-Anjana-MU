from ColorPair_get_data import *
from main import *

def createReferenceManual():
    pair_number_start_index = 1
    pair_number_end_index = 26
    reference_manual = []    
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        color_pair = get_color_from_pair_number(pair_number)
        formatted_colorpair = color_pair_to_string(color_pair[0], color_pair[1])        
        reference_manual.append ("{:<10} {:<10} ".format(pair_number, formatted_colorpair))  
    return reference_manual

def printReferenceManual(refData):
    print ("{:<10} {:<10} ".format('PairNumber', 'ColorPair'))
    for data in refData:
        print(data)
