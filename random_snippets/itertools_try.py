import itertools
import operator
import random


def run_length_encoding(encoded_str):
    output_str = ""
    for char, group in itertools.groupby(encoded_str):
        output_str += char + str(len(list(group)))

    return output_str


def cartesian_product():
    a = ['a', 'b', 'c']
    b = [1, 2]
    c = ['p', 'q', 'r']
    for e in itertools.product(a, b, c, repeat=1):
        print(e)


def accumulate():
    # Example of a geometric progression using itertools accumulate
    array = [2] * 10
    print(list(itertools.accumulate(array, operator.mul)))


def dropwhile():
    array = [0] * 5 + [1] * 5
    random.shuffle(array)
    print("original array: {}".format(array))
    # drop all values to get list of zeroes
    print(list(itertools.dropwhile(lambda x: x != 0, array)))


def flatten():
    array_2d = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(list(itertools.chain(*array_2d)))


def powerset():
    a = [1, 2, 3]
    for item in itertools.chain.from_iterable(itertools.combinations(a, b) for b in range(len(a) + 1)):
        print(item)


def permutation():
    for p in itertools.permutations(range(3)):
        print(p)


def compress():
    # find words in below words list which has values in counts list
    words = "my name is adhithyan".split(" ")
    count = [10, '', None, "ue"]
    print(list(itertools.compress(words, count)))


def main():
    print(run_length_encoding("AABBBBBCCDYYYZZ"))
    cartesian_product()
    accumulate()
    dropwhile()
    flatten()
    powerset()
    permutation()
    compress()


if __name__ == "__main__":
    main()
