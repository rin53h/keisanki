# import pytest
import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.my_library.load_dictionary as dictionary_loader

def test_dictionary1():
    file_path = "/Users/ai/Library/CloudStorage/OneDrive-TheUniversityofTokyo/2024 Year 1/1S/F 計算機プログラミング/Project/data/dictionary1.txt"
    output_path = "output_test_dictionary1.txt"
    f_output = open(output_path, 'w')
    d1 = dictionary_loader.load(file_path)
    for key in d1:
        f_output.write("{} : {}\n".format(key, d1[key]))
    f_output.close()

def test_dictionary2():
    file_path = "/Users/ai/Library/CloudStorage/OneDrive-TheUniversityofTokyo/2024 Year 1/1S/F 計算機プログラミング/Project/data/dictionary2.txt"
    output_path = "output_test_dictionary2.txt"
    f_output = open(output_path, 'w')
    d1 = dictionary_loader.load(file_path)
    for key in d1:
        f_output.write("{} : {}\n".format(key, d1[key]))
    f_output.close()
    
test_dictionary1()
test_dictionary2()