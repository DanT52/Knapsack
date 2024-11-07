from functools import lru_cache

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item(name={self.name}, weight={self.weight}, value={self.value})"



def knapsack(items, max_weight):

    # make a dp array
    dp = [[0] * (max_weight + 1) for _ in range(len(items) + 1)]

    take :
    
    skip :




    @lru_cache(None)
    def maxval_startingwith_notExcced(i, j):
        #base case
        if i >= len(items) or j <= 0:
            return 0 
        # only take if we can
        take = 0
        if j - items[i].weight >= 0:
            take = items[i].value + maxval_startingwith_notExcced(i+1, j-items[i].weight)

        skip = maxval_startingwith_notExcced(i+1,j)
        return max(take, skip)

    return maxval_startingwith_notExcced(0, max_weight)






if __name__ == "__main__":
    max_weight = int(input())

    items = []
    try:
        while True:
            line = input().strip()
            if not line:
                break
            name, weight, value = line.split(';')
            items.append(Item(name, int(weight), int(value)))
    except EOFError:
        pass

    print(knapsack(items, max_weight))

    