from collections import deque

#保留迭代操作中的最后五个元素
def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_line
    previous_line.append(line)
