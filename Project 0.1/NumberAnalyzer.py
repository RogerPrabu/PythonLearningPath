# Project 0.1: Python fundamentals - Number Analyzer

def mean(arr: list[int]):
    if arr:
        return sum(arr)/len(arr)
    raise ValueError

def median(arr: list[int]):
    if arr:
        arr.sort()
        l = len(arr)
        if l % 2 != 0:
            return arr[(l-1)//2]
        else:
            return mean(arr[l//2 - 1: l//2+1])
    raise ValueError

def mode(arr: list[int]):
    if arr:
        counter = {}
        for i in arr:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        max_freq = max(counter.values())
        modes = [max_num for max_num in counter if counter[max_num] == max_freq]
        return modes
    raise ValueError

def range_statistics(arr: list[int]):
    if arr:
        return max(arr) - min(arr)
    raise ValueError

def std_dev(arr: list[int]):
    if arr:
        mean_population = mean(arr)
        summation = 0
        for i in arr:
            summation += (mean_population - i) ** 2
        variance = summation / len(arr)
        return variance ** 0.5
    raise ValueError

# 1st Ranking: 7/10

# Corrections after first ranking:
#   -> Added type hints
#   -> Raising ValueError incase of empty list
#   -> Renamed range to range_statistics
#   -> Sort median array before calculating
#   -> Renamed count to max_num

# 2nd Ranking: 7 -> 8.5/10