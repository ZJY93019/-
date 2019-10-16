#求出前缀平均值
def prefix_average1(s):
    n = len(s)
    a = [0] * n               #创建容器列表
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += s[i]
        a[j] = total / (j + 1)
    return a

def prefix_average2(s):
    n = len(s)
    a = [0] * n
    for j in range(n):
        a[j] = sum(s[0:j+1]) / (j + 1)
    return a

def prefix_average3(s):
    n = len(s)
    a = [0] * n
    total = 0
    for j in range(n):
        total += s[j]
        a[j] = total / (j + 1)
    return a
if __name__ == "__main__":
    print(prefix_average1([i for i in range(1, 11)]))
    print(prefix_average2([i for i in range(1, 11)]))
    print(prefix_average3([i for i in range(1, 11)]))
