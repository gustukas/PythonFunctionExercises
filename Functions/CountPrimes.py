def count_primes(num):
    primelist = []
    if num < 2:
        return 0
    for i in range(2,num):
        is_prime = True
        for j in range(3,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            primelist.append(i)
    return len(primelist)


print(count_primes(100000))


