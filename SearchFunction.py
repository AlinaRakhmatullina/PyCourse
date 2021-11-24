def find_most_in_list(list):
    rez = sorted(list, key=lambda x:x[4])[-1]
    return rez

def find_most_in_dict(dict):
    s = str(input())
    sorted_dict = {
        k:v
        for k,v in sorted(dict.items(), key=lambda x:x[1][s])
}

    last = list(sorted_dict.keys())[-1]
    return last, dict[last]


