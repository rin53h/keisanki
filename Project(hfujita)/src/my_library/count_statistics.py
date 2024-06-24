import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root_path)
import src.my_library.tokenizer as tokenizer

def count(d,sequence):
    N = 9
    cnt = [0, 0]
    while len(sequence) > 0:
        print(sequence)
        length = len(sequence)
        search_len = min(N, length)
        for i in range(search_len, 0, -1):
            entry = ('').join(sequence[:i])
            if entry in d:
                if i < length and sequence[i] in ["ない", "ぬ", "無い"]:
                    if d[entry] == "positive":
                        cnt[1] += 1
                    elif d[entry] == "negative":
                        cnt[0] += 1
                    del sequence[:(i + 1)]
                else:
                    if d[entry] == "positive":
                        cnt[0] += 1
                    elif d[entry] == "negative":
                        cnt[1] += 1
                    del sequence[:i]
                break
            if i == 1:
                del sequence[0]
    return cnt
