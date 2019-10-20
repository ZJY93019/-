def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

if __name__ == "__main__":
    import random
    print(sum([i for i in range(10)]))
