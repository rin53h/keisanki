# import pytest
import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.my_library.load_dictionary as dictionary_loader

file_path = f"{project_root_path}/data/dictionary1.txt"
output_path = "output_test_dictionary1.txt"
d1 = {}
d1 = dictionary_loader.load(file_path, d1)

file_path = f"{project_root_path}/data/dictionary2.txt"
output_path = "output_test_dictionary.txt"
f_output = open(output_path, 'w')
d1 = dictionary_loader.load(file_path, d1)
for key in d1:
    f_output.write("{} : {}\n".format(key.strip("\""), d1[key]))
f_output.close()
    