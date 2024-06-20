def load(file_name):
    f = open(file_name, 'r')
    dictionary = {}
    
    if file_name[-5] == '1':
        for line in f:
            line = line[:-1].split()
            word = line[0]
            if line[1] == "n":
                dictionary[word] = 'negative'
            elif line[1] == 'p':
                dictionary[word] = 'positive'
            elif line[1] == 'e':
                dictionary[word] = 'neutral'
    elif file_name[-5] == '2':
        uuu = ['う','く','す','つ','ぬ','ふ','む','る','ぶ']
        for line in f:
            line = line[:-1].split()
            if len(line) > 1:
                word = line[1] # not done / wrong way
                dictionary[word] = 'negative' if 'ネガ' in line[0] else 'positive'

    f.close()
    return dictionary