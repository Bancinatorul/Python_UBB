import random

def create_random_list(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(0, 100))
    return random_list

def binary_search(x, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == x:
            return middle
        elif array[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def print_the_step_list(array, step):
    if step % 10 == 1 and step % 100 != 11:
        print(f"{step}'st step: {array}")
    elif step %  10 == 2 and step % 100 != 12:
        print(f"{step}'nd step: {array}")
    elif step % 10 == 3 and step % 100 != 13:
        print(f"{step}'rd step: {array}")
    else:
        print(f"{step}'th step:  {array}")

def bubble_sort(array, given_step):
    # I will consider the step to be the swap
    sorted_for_bubble = False
    step = 0
    while not sorted_for_bubble:
        sorted_for_bubble = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                step += 1
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted_for_bubble = False
            if step % given_step == 0:
                print_the_step_list(array, step)
    return array

def heapify(array, n, i, step, given_step):
    largest = i
    if i * 2 + 1 < n  and array[i * 2 + 1] > array[largest]:
        largest = i * 2 + 1
    if i * 2 + 2 < n and array[i * 2 + 2] > array[largest]:
        largest = i * 2 + 2
    if largest != i:
        step += 1
        array[i], array[largest] = array[largest], array[i]
        if step % given_step == 0:
            print_the_step_list(array, step)
        heapify(array, n, largest, step, given_step)
    return step

def heap_sort(array, given_step):
    # I will consider the step to be the swap
    n = len(array)
    step = 0
    for i in range(n // 2 - 1, -1 , -1):
        step = heapify(array, n, i, step, given_step)
    for i in range(n - 1, 0, -1):
        step += 1
        array[0], array[i] = array[i], array[0]
        step = heapify(array, i, 0, step, given_step)
        if step % given_step == 0:
            print_the_step_list(array, step)
    return array

def print_menu():
    print("MENU:")
    print("1. Generate a list of n random elements")
    print("2. Binary search for a given number")
    print("3. Bubble sort")
    print("4. Heap sort")
    print("0. Exit")

def start():
    step = 0
    sorted = False
    existing_list = False
    while True:
        print_menu()
        op = int(input(">> "))
        if op == 1:
            sorted = False
            length = int(input("Give the length of the list: "))
            my_array = create_random_list(length)
            if length > 0:
                existing_list = True
            print("Here is the random list: ")
            print(my_array)
        elif op == 2:
            if not sorted or not existing_list:
                print("If you want to search, you firstly have to create and sort the list!")
            else:
                given_number = int(input("The number you are looking for is: "))
                position = binary_search(given_number, my_array)
                if position != -1:
                    print(f"The number {given_number} is at position {position + 1}")
                else:
                    print(f"The number {given_number} doesn't appear in the list")
        elif op == 3:
            if not existing_list:
                print("If you want to sort, you firstly have to create the list!")
            else:
                given_step = int(input("Give the step: "))
                my_array = bubble_sort(my_array, given_step)
                sorted = True
                print("Here is the sorted list: ")
                print(my_array)
        elif op == 4:
            if not existing_list:
                print("If you want to sort, you firstly have to create the list!")
            else:
                given_step = int(input("Give the step: "))
                my_array = heap_sort(my_array, given_step)
                sorted = True
                print("Here is the sorted list: ")
                print(my_array)
        elif op == 0:
            break
        else:
            print("Please select a valid option!")

if __name__ == "__main__":
    start()