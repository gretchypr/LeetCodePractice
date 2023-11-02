
def canCompleteCircuit(gas, cost):
    # results = [i for i in range(len(gas)) if gas[i] - cost[i] >= 0]
    if len(gas) == 1:
        return -1 if gas[0] - cost[0] < 0 else 0
    results = [gas[i]-cost[i] for i in range(len(gas))]
    i = 0
    j = 1
    sum = results[i]
    while i < len(results) and j!= i:
        if sum < 0:
            if j > i:
                i = j
                j = (i + 1) % len(results)
                sum = results[i]
            else:
                return -1
        else:
            sum += results[j]
            j = (j + 1) % len(results)
        
    if sum >= 0:
        return i
    return -1

def test1():
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    return canCompleteCircuit(gas, cost)

def test2():
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    return canCompleteCircuit(gas, cost)

if __name__ == "__main__":
    print(test1())
    print(test2())