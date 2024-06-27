import MeCab
import ipadic

def tokenize(text):
    tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
    parsed_text = tagger.parse(text)

    tokens = []
    for line in parsed_text.splitlines()[:-1]:  # 最後の空行を除外
        if line == 'EOS':
            continue
        surface, feature = line.split('\t')
        base_form = feature.split(',')[6] #原型を取得

        if base_form == '*':
            base_form = surface #用言でない場合は表層形を取得

        tokens.append((base_form))

    return tokens