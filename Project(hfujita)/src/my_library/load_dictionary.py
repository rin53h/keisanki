import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root_path)
import src.my_library.tokenizer as tokenizer

def load(file_name, dictionary):
    f = open(file_name, 'r')
    if file_name[-5] == '1':
        for line in f:
            line = line[:-1].split()
            word = line[0]
            if line[1] == "n":
                dictionary[word] = "negative"
            elif line[1] == 'p':
                dictionary[word] = "positive"
            elif line[1] == 'e':
                dictionary[word] = "neutral"
            if len(line) > 2:
                if "主観" in line[2] and word in dictionary:
                    dictionary[word] += "strong"
    elif file_name[-5] == '2':
        for line in f:
            line = line[:-1].split()
            if 2 <= len(line):
                pre_words = ""
                for i in range(1, len(line)):
                    pre_words += line[i]
                tokens = tokenizer.tokenize(pre_words)
                words = ""
                for i in range(len(tokens)):
                    words += tokens[i]
                dictionary[words] = "negative" if 'ネガ' in line[0] else "positive"
                if "経験" in line[0]:
                    dictionary[words] += "strong"

    f.close()
    return dictionary