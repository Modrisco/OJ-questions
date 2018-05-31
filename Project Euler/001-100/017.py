def find_sub(w):
    if len(set(w)) == 1:
        return ['', w[0]]
    sub = find_sub(w[1:])
    cur_str = []
    for i in range(len(sub)):
        if cur_str not in sub and w[0] not in sub[i]:
            cur_str.append(w[0] + sub[i])
        
    return sub + cur_str
