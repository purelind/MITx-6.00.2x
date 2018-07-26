import random


def deterministicNumber():
    '''
    Deterministically g
    :return:
    '''
    return list(i for i in range(9, 21) if i % 2 == 0)[1]


if __name__ == '__main__':
    print(deterministicNumber())
