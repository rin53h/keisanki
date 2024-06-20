def output(sentence_arrays, result):
    file_path = "/Users/ai/Library/CloudStorage/OneDrive-TheUniversityofTokyo/2024 Year 1/1S/F 計算機プログラミング/Project/logs/output.txt"
    f = open(file_path, 'w')
    for i in range(len(sentence_arrays)):
        sentence = sentence_arrays[i]
        f.write("Output #{}\n".format(i))
        f.write(sentence+'\n')
        f.write("Polarity = {}\n\n".format(result[i]))
    f.close()
    return