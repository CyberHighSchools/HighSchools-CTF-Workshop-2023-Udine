def apply_permutation(list_of_bits, permutation):
    temp=[list_of_bits[i] for i in permutation]
    return temp

def round(list_of_bits, permutation):
    temp = apply_permutation(list_of_bits, permutation)
    return temp

# value is a binary string representing a number which is the secret
def encrypt(value, permutations):
    ROUNDS = len(permutations)
    # make the list of bits from value
    list_of_bits = [i for i in value]

    # applying permutations to list_of_bits
    for i in range(ROUNDS):
        list_of_bits = round(list_of_bits, permutations[i])
    
    # convert binary list to integer
    binary = "".join([str(i) for i in list_of_bits]).zfill(8)
    return binary

def reverse_permutation(permutation):
    temp = [0 for _ in range(len(permutation))]
    for i in range(len(permutation)):
        temp[permutation[i]] = i
    
    return temp

def reverse_permutations(permutations):
    reversed = []
    for i in range(len(permutations)-1, -1, -1):
        reversed.append(reverse_permutation(permutations[i]))
    return reversed
    