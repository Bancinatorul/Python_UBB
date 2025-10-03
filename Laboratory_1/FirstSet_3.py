"""
For a given natural number n find the minimal natural number m formed with the same digits.
(e.g. n=3658, m=3568).
"""

def number_into_list(n):
    digit = []
    if n == 0:
        digit.append(n)
    while n:
        digit.append(n % 10)
        n //= 10
    return digit

def sort(array):
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

def max_number(array):
    max_num = 0
    for i in array:
        max_num = max_num * 10 + i
    return max_num

if __name__ == "__main__":
    num = int(input("Give the number: "))
    digits = number_into_list(num)
    sort(digits)
    print("The maximum number is: ", max_number(digits))

