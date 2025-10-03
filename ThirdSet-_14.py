"""
Determine the n-th element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,...
obtained from the sequence of natural numbers by replacing composed numbers with their prime divisors,
each divisor d being written d times, without memorizing the elements of the sequence.
"""

def prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False
    d = 3
    while d * d <= num:
        if num % d == 0:
            return False
        d += 2
    return True

def prime_divisors(n, pos):
    d = 2
    while n != 1:
        divisor = False
        while pos and n % d == 0:
            n //= d
            divisor = True
        if divisor:
            pos -= d
            if pos <= 0:
                return d, 0
        d += 1
    return None, pos

if __name__ == "__main__":
    position = int(input("Give the position: "))
    if position == 1:
        print(1)
    else:
        position -= 1
        number = 2
        number_to_print = number
        while position:
            if prime(number):
                number_to_print = number
                position -= 1
            else:
                number_to_print, position = prime_divisors(number, position)
            number += 1
        print(number_to_print)
