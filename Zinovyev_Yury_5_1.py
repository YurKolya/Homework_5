""" task 1"""

def odd_num(to):
    for i in range(1, to + 1, 2):
        yield i

if __name__ == "__main__":
    a_gen = odd_num(15)

    print("a_gen type", type(a_gen))

    for elem in a_gen:
        print(elem)

    print(f"empty {list(a_gen)}")
