permutations = [
    [4, 1, 0, 3, 5, 2, 6, 7],
    [2, 6, 7, 0, 1, 3, 5, 4] ,
    [5, 2, 3, 7, 4, 0, 1, 6] ,
    [2, 6, 0, 3, 4, 7, 5, 1],
    [1, 2, 0, 4, 7, 5, 6, 3]
]

def reverse_permutation(permutation):
    temp = [0 for _ in range(len(permutation))]
    for i in range(len(permutation)):
        temp[permutation[i]] = i
    
    return temp

for i in range(4, -1, -1):
    print(reverse_permutation(permutations[i]))