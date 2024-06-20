import os
import sys
print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))) # file directory
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)

import my_library.load_input_data as input_loader
import my_library.load_dictionary as dictionary_loader
import my_library.count_statistics as counter
import my_library.predict_polarity as predictor
import my_library.manage_output as output_manager

sentence_arrays = input_loader.load("/Users/ai/Library/CloudStorage/OneDrive-TheUniversityofTokyo/2024 Year 1/1S/F 計算機プログラミング/Project/data/data.txt")

d1 = dictionary_loader.load("/Users/ai/Library/CloudStorage/OneDrive-TheUniversityofTokyo/2024 Year 1/1S/F 計算機プログラミング/Project/data/dictionary1.txt") # dict 1 file
d2 = dictionary_loader.load("/Users/ai/Library/CloudStorage/OneDrive-TheUniversityofTokyo/2024 Year 1/1S/F 計算機プログラミング/Project/data/dictionary2.txt") # dict 2 file

result = []
for sentence in sentence_arrays:
    count_statistics = counter.count(d1,d2,sentence)
    # count_statistics = [2,1]
    result.append( predictor.predict(count_statistics) )

output_manager.output(sentence_arrays, result)