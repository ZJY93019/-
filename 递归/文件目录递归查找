import os
def disk_usage(path):
    total = os.path.getsize(path)
    #返回字符串路径
    if os.path.isdir(path):
    #指定条目为目录，则返回True
        for filename in os.listdir(path):
            #返回一个字符串列表
            childpath = os.path.join(path, filename)
            #生成路径字符串和文件名字符串
            total += disk_usage(childpath)
            #统计文件总数量
    return total
