from janome.tokenizer import Tokenizer # type:ignore

def count_and_vectorize(dic, sent):
    tokenizer = Tokenizer()
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    words = []
    for token in tokenizer.tokenize(sent):
        words.append(token.base_form)

    for key in dic:        
        if key in words:
            if dic[key] == "n":
                num_negative += 1
            elif dic[key] == "p":
                num_positive += 1
            elif dic[key] == "e":
                num_neutral += 1
    num_total = num_negative + num_positive + num_neutral 
    
    return [num_positive, num_negative, num_neutral, num_total]


