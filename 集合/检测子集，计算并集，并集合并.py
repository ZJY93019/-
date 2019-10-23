#子集检测
def __It__(self, other):
    if len(self) >= len(other):
        return False
    for e in self:
        if e not in other:
            return False
    return True

#并集计算
def __or__(self, other):
    result = type(self)()
    for e in self:
        result.add(e)
    for e in other:
        result.add(e)
    return result

#集合合并
def __ior__(self, other):
    for e in other:
        self.add(e)
    return self
