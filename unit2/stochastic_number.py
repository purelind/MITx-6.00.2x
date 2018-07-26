import random


def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed enen
    number between 9 and 21
    :return:
    '''
    return random.choice(list(i for i in range(9, 21) if i % 2 == 0))


if __name__ == '__main__':
    print(stochasticNumber())
