import time

def recursive(i):
    l = [i for i in range(2)]
    if i == 0:
        return None
    return recursive(i - 1)

recursive(1000)