import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root_path)
import src.my_library.tokenizer as tokenizer

japanese_conjunctions = [
    "けど", "しかし", "だが", "ですが", "さりながら", "しかるに",
    "けれども", "けれど", "だけれども", "だけれど", "だけども", "だけど",
    "ものの", "とはいうものの", "とはいえ", "とはいっても",
    "不当", "しかしながら",
    "ところが",
    "にもかかわらず", "それにもかかわらず", "のに", "なのに", "それなのに",
    "でも", "それでも", "それでもなお"
]

def count(d,sequence):
    N = 9
    cnt = [0, 0]
    flag = False
    while len(sequence) > 0:
        length = len(sequence)
        search_len = min(N, length)
        for i in range(search_len, 0, -1):
            entry = ('').join(sequence[:i])
            if entry in d:
                if i < length and sequence[i] in ["ない", "ぬ", "無い"]:
                    if "positive" in d[entry]:
                        cnt[1] += 2
                        if flag == True:
                            cnt[1] += 2
                        if "strong" in d[entry]:
                            cnt[1] += 1
                    elif "negative" in d[entry]:
                        cnt[0] += 2
                        if flag == True:
                            cnt[0] += 2
                        if "strong" in d[entry]:
                            cnt[0] += 1
                    del sequence[:(i + 1)]
                else:
                    if "positive" in d[entry]:
                        cnt[0] += 2
                        if flag == True:
                            cnt[0] += 2
                        if "strong" in d[entry]:
                            cnt[0] += 1
                    elif "negative" in d[entry]:
                        cnt[1] += 2
                        if flag == True:
                            cnt[1] += 2
                        if "strong" in d[entry]:
                            cnt[1] += 1
                    del sequence[:i]
                break
            if i == 1:
                if sequence[0] in japanese_conjunctions:
                    flag = True
                del sequence[0]
    return cnt
