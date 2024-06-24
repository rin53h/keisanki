def predict(count_stat):
    if len(count_stat) == 0: return 'neutral'
    if count_stat[0] > count_stat[1]: return 'positive'
    if count_stat[0] < count_stat[1]: return 'negative'
    return 'neutral'