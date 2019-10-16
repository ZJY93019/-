def unique1(S):
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False
    return True

def unique2(S):
    temp = sorted(S)
    #进行排序，这样子只需要验证第一个跟第二个是否相等
    for j in range(1, len(temp)):
        if temp[j-1] == temp[j]:
            return False
    return True

if __name__ == "__main__":
    print(unique1([i for i in range(1, 11)]))
    print(unique2([i for i in range(1, 11)]))
