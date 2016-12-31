def is_prime(n):    
    if n < 2:
        return False    
    elif n == 2:
        return True    
    else:
        flag = 1
        for t in range(2, n):
            if n%t == 0:
                flag = 0
                break
        if flag == 1:
            return True
        else:
            return False
NumberPrimes = 0
Upper = raw_input("test primes upto")
Upper = int(Upper)
for m in range(0,Upper+1):
    if is_prime(m) == True:
        NumberPrimes = NumberPrimes + 1
        print m
print NumberPrimes, "primes upto", Upper
