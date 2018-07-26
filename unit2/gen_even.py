import random


def genEven():
    '''
    Return a random even number x, where 0<= x < 100
    :return:
    '''
    return random.choice(list(i for i in range(100) if i % 2 == 0))


if __name__ == '__main__':
    print(genEven())
