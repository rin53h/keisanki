import os
import sys
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)   

import my_library.load_input_data as input_loader
import my_library.load_dictionary as dictionary_loader
from my_library.Data_preprocessor import DataPreprocessor

logs_path = "_logs/pre1"

# data_path = input("Enter the path for the data file: ")
# dictionary_path = input("Enter the path for the dictionary file: ")
# preprocessed_data_path = input("Enter the path to save the preprocessed data: ")

dictionary_path1 = "data/dictionary1.txt"
dictionary_path2 = "data/dictionary2.txt"

# data_path = "data/data.txt"
# preprocessed_data_path = "data/data_preprocessed.pkl"
# data_path = "data/train.txt"
# preprocessed_data_path = "data/train_preprocessed.pkl"
# data_path = "data/validation.txt"
# preprocessed_data_path = "data/validation_preprocessed.pkl"
data_paths = ["data/train.txt", 
              "data/validation.txt",
              "data/data.txt"]
preprocessed_data_paths = ["data/train_preprocessed.pkl", 
                          "data/validation_preprocessed.pkl",
                          "data/data_preprocessed.pkl"]
labeled = ['Y','Y','N']

# labeled = input("Enter if the data is labeled (Y/N):")

dict1 = dictionary_loader.load(dictionary_path2)
dict2 = dictionary_loader.load(dictionary_path2)
dictionary = {**dict1, **dict2} # join dict1, dict2 -> dict

for i in range(len(data_paths)):
    if i<=1: continue
    data_path = data_paths[i]
    preprocessed_data_path = os.path.join(logs_path, preprocessed_data_paths[i])

    if labeled[i] == "Y":
        sentence_arrays = input_loader.load(data_path)
        data_preprocessor = DataPreprocessor(sentence_arrays[1:], dictionary)
        data_preprocessor.preprocess_data_and_label()
    else:
        sentence_arrays = input_loader.load_raw_data(data_path)
        data_preprocessor = DataPreprocessor(sentence_arrays, dictionary)
        data_preprocessor.preprocess_data()

    data_preprocessor.dump(preprocessed_data_path)