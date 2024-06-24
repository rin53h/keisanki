def load(file_path):
    f = open(file_path, 'r')
    sentence_arrays = []
    for line in f:
        sentence_arrays.append(line[:-1])
    f.close()
    return sentence_arrays