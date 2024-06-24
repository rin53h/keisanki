import os
import sys
# print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))) # file directory
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)

import my_library.load_input_data as input_loader
import my_library.load_dictionary as dictionary_loader
import my_library.count_statistics as counter
import my_library.predict_polarity as predictor
import my_library.manage_output as output_manager
import my_library.tokenizer as tokenizer

sentence_arrays = input_loader.load(f"{project_root_path}/data/data.txt")

d = {}
d = dictionary_loader.load(f"{project_root_path}/data/dictionary1.txt", d) # dict 1 file
d = dictionary_loader.load(f"{project_root_path}/data/dictionary2.txt", d) # dict 2 file

result = []
for sentence in sentence_arrays:
    sequence = tokenizer.tokenize(sentence)
    count_statistics = counter.count(d,sequence)
    # count_statistics = [2,1]
    result.append( predictor.predict(count_statistics) )

output_manager.output(sentence_arrays, result)