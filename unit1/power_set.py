# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            # bit i 中如果第i位是1，表示选择该item,添加到combo列表中
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

print(list(powerSet([1, 2, 3])))

# 如果items = [1, 2, 3], 那么len(items) --> 3
# 那么i --> 00000000(N位) -- 11111111(N位)，每一个位置代表一个item的状态：0-->不选择，1-->选择
# 而j的范围：0 --> N-1共N个数

