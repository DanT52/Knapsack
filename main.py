# from functools import lru_cache

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item(name={self.name}, weight={self.weight}, value={self.value})"



def knapsack(items, max_weight):

    #iterative

    # make a dp array

    #now lets make dp also store the curret items we are taking
    # and their current value

    #so each dp entry will be like
    # [set(items taking), weight, value]

    dp1 = [(set(), 0, 0) for _ in range(max_weight + 1)]

    for i in range(len(items) - 1, -1, -1):
        for j in range(max_weight, 0, -1):

            take = 0
            if j - items[i].weight >= 0:
                take = items[i].value + dp1[j-items[i].weight][1]

            skip = dp1[j][1]
            if take > skip:
                dp1[j] = (dp1[j-items[i].weight][0] | {i}, take, dp1[j-items[i].weight][2] + items[i].weight)

    
    return dp1[max_weight]



    # recursive version only return the max value    
    # @lru_cache(None)
    # def maxval_startingwith_notExcced(i, j):
    #     #base case
    #     if i >= len(items) or j <= 0:
    #         return 0 
    #     # only take if we can
    #     take = 0
    #     if j - items[i].weight >= 0:
    #         take = items[i].value + maxval_startingwith_notExcced(i+1, j-items[i].weight)

    #     skip = maxval_startingwith_notExcced(i+1,j)
    #     return max(take, skip)

    # return maxval_startingwith_notExcced(0, max_weight)

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
 

    used, value, weight = knapsack(items, max_weight)
 

    # Create a dictionary to count the occurrences of each item
    item_counts = {}
    for i in used:
        item_key = (items[i].name, items[i].weight, items[i].value)
        if item_key in item_counts:
            item_counts[item_key] += 1
        else:
            item_counts[item_key] = 1
    
    # Create a list to store the items in the order they appear in the input
    ordered_items = []
    for item in items:
        item_key = (item.name, item.weight, item.value)
        if item_key in item_counts and item_counts[item_key] > 0:
            ordered_items.append(item)
            item_counts[item_key] -= 1
    
    for item in ordered_items:
        print(f"{item.name}, {item.weight}, {item.value}")

    print("final weight: " + str(weight))
    print("final value: " + str(value))