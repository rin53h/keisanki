def count(d1,d2,sentence):
    cnt = [0,0]
    for word in d1:
        if word in sentence:
            if d1[word] == 'positive': cnt[0] += 1
            elif d1[word] == 'negative': cnt[1] += 1
    for word in d2:
        if word in sentence:
            if d2[word] == 'positive': cnt[0] += 1
            elif d2[word] == 'negative': cnt[1] += 1
    return cnt