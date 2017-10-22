# decision tree implementation
# 决策树实现0/1背包问题


def maxVal(toConsider, avail):
    """Assumes toConsider --> a list of items,
                avail --> a weight
        Return --> a tuple of the total value of a
            solution to 0/1 knapsack problem and
            the items of that solution
        toConsider: 列表表示的物品
        avail: 允许携带的重量
        Return: 元组，背包问题的解决方案和该方案包含的具体物品"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        # 若第一个物品重量大于允许携带的最大重量，则不可能携带该物品，
        # 只探索右侧决策树，即： No this item
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        # 携带第一个物品
        # 注意将第一个物品的价值加入
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail-nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        # 不携带第一个物品
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def testMaxVal(foods, maxUnits, printItems=True):
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print(' ', item)


import random

class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ": <" + str(self.value)\
                + "," + str(self.calories) + '>'


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

for numItems in range(5, 50, 5):
    print('Try a menu with', numItems, 'items')
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, False)
