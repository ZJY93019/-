def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

def merge_sort(s):
    n = len(s)
    if n < 2:
        return False
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    merge_sort(s1) #进行分治，递归
    merge_sort(s2)
    merge(s1, s2, s)

if __name__ == "__main__":
    import random
    # s1 = [1, 2, 3, 8]
    # s2 = [2.5, 4, 5, 6]
    # s = [None] * (len(s1) + len(s2))
    # merge(s1, s2, s)
    # print(s)
    s = [random.randrange(10**10) for _ in range(10**1) ]
    print(s)
    merge_sort(s)
    print(s)
