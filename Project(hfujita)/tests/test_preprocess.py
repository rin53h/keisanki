import MeCab
import ipadic
import os

def tokenize(text):
    tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
    parsed_text = tagger.parse(text)

    tokens = []
    for line in parsed_text.splitlines()[:-1]:  # 最後の空行を除外
        if line == 'EOS':
            continue
        # 形態素解析結果から単語とその他の情報を取得
        surface, feature = line.split('\t')
        pos = feature.split(',')[0]  # 品詞情報から品詞の部分を取得
        base_form = feature.split(',')[6]  # 原型（基本形）を取得

        if base_form == '*':
            base_form = surface

        tokens.append((base_form))

    return tokens

# def load(file_name):
#     f = open(file_name, 'r')
#     dictionary = {}
    
#     if file_name[-5] == '1':
#         for line in f:
#             line = line[:-1].split()
#             word = line[0]
#             if line[1] == "n":
#                 dictionary[word] = 'negative'
#             elif line[1] == 'p':
#                 dictionary[word] = 'positive'
#             elif line[1] == 'e':
#                 dictionary[word] = 'neutral'
#     elif file_name[-5] == '2':
#         for line in f:
#             line = line[:-1].split()
#             if 2 <= len(line):
#                 words = ""
#                 for i in range(1, len(line)):
#                     words += line[i]
#                 dictionary[word] = 'negative' if 'ネガ' in line[0] else 'positive'

#     f.close()
#     return dictionary

# project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
# file_path = f"{project_root_path}/data/processed_data.txt"
# f = open(file_path, 'w')
# for i in range(len(sentence_arrays)):
#     sentence = sentence_arrays[i]
#     f.write("Output #{}\n".format(i))
#     f.write(sentence+'\n')
#     f.write("Polarity = {}\n\n".format(result[i]))
# f.close()
# テスト用のテキスト
text = "褒める、ほめる"

# 形態素解析と原型変換を行う
tokens = tokenize(text)

print((" ").join(tokens))
tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
print(tagger.parse(text))
