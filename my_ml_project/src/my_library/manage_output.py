import os

def output(sentence_arrays, result):
    project_root_path = os.path.dirname(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )))
    file_path = f"{project_root_path}/logs/output.txt"
    f = open(file_path, 'w')
    for i in range(len(sentence_arrays)):
        sentence = sentence_arrays[i]
        f.write("Output #{}\n".format(i))
        f.write(sentence+'\n')
        f.write("Polarity = {}\n\n".format(result[i]))
    f.close()
    return