def semiPrimes(n, p, q):
    # Prime
    primes = []
    for x in range(1, n):
        if (x % 1 == 0) & (x % x == 0) & (x != 1):
            if ((x % 2 != 0) & (x % 3 != 0) & (x % 5 != 0) & (x % 7 != 0)) | (x == 2) | (x == 3) | (x == 5) | (x == 7):
                primes.append(x)

    # Semi-Prime
    semi_primes = []
    primes_2 = primes
    for x in primes:
        for y in primes:
            criterion = x * y
            if criterion not in semi_primes:
                semi_primes.append(criterion)
    semi_primes.sort()

    # Query K
    finals = []
    for index in range(len(p)):
        valid_semis = [x for x in semi_primes if (x >= p[index]) & (x <= q[index])]
        finals.append(len(valid_semis))

    return finals


print(semiPrimes(26, [1, 4, 16], [26, 10, 20]))
