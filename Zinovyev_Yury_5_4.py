""" task 4 """


import time
import sys


def my_filter(*argv):
    return(argv[i] for i in range(1, len(argv)) if argv[i] > argv[i - 1])
    return (y for (x, y) in zip(argv[:-2], argv[1:]) if x < y)  # best
    # return (argv[i] for i in range(1, len(argv)) if argv[i] > argv[i - 1])



if __name__ == "__main__":

    scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [12, 44, 4, 10, 78, 123]

    t = time.perf_counter()
    answ = my_filter(*scr)
    print(time.perf_counter() - t)
    print(sys.getsizeof(answ))
    print(list(answ) == result)  # we don't know assert for test