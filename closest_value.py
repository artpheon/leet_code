from random import randint
from random import seed
import time

def counter(closest_func):
    def wrapper(arrayA, arrayB, value):
        t0 = time.time()
        ret = closest_func(arrayA, arrayB, value)
        print("spent time in seconds: {}".format(round(time.time()-t0, 3)))
        return ret
    return wrapper

# def closest_pairs(arrayA, arrayB, value):
#     pairs = {}
#     diff = float('inf')
#     for A in arrayA:
#         for B in arrayB:
#             tmp = abs(A + B - value)
#             if tmp <= diff:
#                 diff = tmp
#                 if diff in pairs.keys():
#                     pairs[diff].append((A, B))
#                 else:
#                     pairs[diff] = [(A, B)]
#     key = list(set(pairs.keys()))[0]
#     return pairs[key]

@counter
def closest_pairs(arrayA, arrayB, value):
    diff = float('inf')
    for A in arrayA:
        for B in arrayB:
            tmp = abs(A + B - value)
            if tmp <= diff:
                diff = tmp
                pair = (A, B)
    return pair


def closest_pairs_2(arrayA, arrayB, value):
    pairs = []
    look = value
    search = set(arrayB)
    i = 1
    while len(pairs) == 0:
        for el in arrayA:
            if look - el in search:
                pairs.append((el, look - el))
        if i > 0:
            i = 0 - i
        else:
            i = (0 - i) + 1
        look = look + i
    return pairs

@counter
def closest_pairs_3(arrayA, arrayB, value):
    arrayA = sorted(arrayA)
    arrayB = sorted(arrayB)
    x = 0
    y = len(arrayB) - 1
    smallest_diff = abs(arrayA[x] + arrayB[y] - value)
    while x < len(arrayA) and y >= 0:
        A = arrayA[x]
        B = arrayB[y]
        diff = A + B - value
        if abs(diff) < smallest_diff:
            smallest_diff = abs(diff)
            pair = (A, B)
        if diff == 0:
            return pair
        elif diff < 0:
            x = x + 1
        else:
            y = y - 1
    return pair
    

def random_array(highest, size, s=666):
    seed(s)
    array = []
    for _ in range(size):
        array.append(randint(0, highest))
    return array


# arrayA = [-1, 3, 8, 2, 9, 5]
# arrayB = [4, 1, 2, 10, 5, 20]
print("Creating arrays with random numbers...")
arrayA = random_array(2000000, 10000000, 7)
arrayB = random_array(2000000, 10000000, 34)
value = 10000

# pair = closest_pairs(arrayA, arrayB, value)

# print("Solution 1:\n{}".format(pair))


print("\nSolution 3 calculating:")
pair = closest_pairs_3(arrayA, arrayB, value)
print(pair)