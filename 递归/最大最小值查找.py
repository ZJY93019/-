def find_max(s,start,stop):
    if s[start] > s[stop]:
        return find_max(s, start, stop-1)  #max
    elif s[start] < s[stop]:
        return find_max(s, start+1, stop)  #max
    else:
        return s[stop]

def find_min(s, start, stop):
    if s[start] > s[stop]:
        return find_min(s, start+1, stop)
    elif s[start] < s[stop]:
        return find_min(s, start, stop-1)
    else:
        return s[start]

def find_mm(s):
    min = find_min(s, 0, len(s)-1)
    max = find_max(s, 0, len(s)-1)
    return min, max

if __name__ == "__main__":
    s = [18,4,6,48,4,6,72,7,4,94]
    print(find_mm(s))
