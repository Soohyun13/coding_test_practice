from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    candidates = set()

    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int(''.join(p)) 
            candidates.add(num)

    count = 0
    for num in candidates:
        if is_prime(num):
            count += 1
    return count