def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    # i --> bag1, j --> bag2, 需要排除item同时出现在bag1,bag2的情况
    for i in range(2**N):
        for j in range(2**N):
            combo = (list(), list())
            for k in range(N):
                if (i >> k) % 2 == 1:
                    combo[0].append(items[k])
                if (i >> k) % 2 == 0 and (j >> k) % 2 == 1:
                    combo[1].append(items[k])
            yield combo


print(list(yieldAllCombos([1, 2, 3])))

# With two bags, there are 3^n possible combinations available.

# With one bag we determined there were 2n possible combinations available by
# representing the bag as a list of binary bits, 0 or 1. Since there are N
# bits, and they can be one of two possibilities, there must be 2n possibilities.

# With two bags there thus must be 3n possible combinations. You can imagine this
# by representing the two bags as a list of "trinary" bits, 0, 1, or 2 (a 0 if
# an item is in neither bag; 1 if it is in bag1; 2 if it is in bag2). With
# the "trinary" bits, there are N bits that can each be one of three
# possibilities - thus there must be 3n possible combinations.
