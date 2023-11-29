import numpy as np

def prime_factors(n: int):
    number_of_divisors = 0
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            number_of_divisors+=1
            factors.append(i)
            other = n // i #check reciprocal
            if not other == i and not other ==n : #dont include i or n
                number_of_divisors+=1
                factors.append(other)
    factors.sort()
    return factors

def permutate(input: list):
    if not input:
        return input
    elif len(input) == 1:
        return [input]

    all_permutations = []
    if len(all_permutations) >= 1e6-1:
        return all_permutations
    for digit in input:
        other_digits = [x for x in input if x != digit]
        for permutations in permutate(other_digits):
            all_permutations.append([digit] + permutations)
    return all_permutations