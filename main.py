# 6 Sorting Alogrithms
# Written by Dakota McGuire 3/1/19


def merge_sort(array):
    temp_array = array
    if not array:
        print("Empty Array")
    if len(array) == 1:
        print(array)
    else:
        length = len(array)
        if length > 1:
            middle = length // 2
            left = array[0, middle]
            right = array[middle, length]
            merge_sort(left)
            merge_sort(right)

        count_left = 0  # left array index
        count_right = 0  # Right array index
        count_merge = 0  # Merged array index

        while count_left < len(left) and count_right < len(right):
            if left[count_left] < right[count_right]:
                temp_array[count_merge] = left[count_left]
                count_left = count_left + 1
            elif left[count_left] > right[count_right]:
                temp_array[count_merge] = right[count_right]
                count_right = count_right + 1
            count_merge = count_merge + 1

        while count_left < len(left):
            temp_array[count_merge] = left[count_left]
            count_merge = count_merge + 1
            count_left = count_left + 1

        while count_right < len(right):
            temp_array[count_merge] = left[count_right]
            count_merge = count_merge + 1
            count_right = count_right + 1
        print(temp_array)
    pass


def quick_sort(array):
    print("Insertion sort: ")
    print("------------------")
    if not array:
        print("Empty Array")
    if len(array) == 1:
        print(array)
    pass


def insertion_sort(array):
    print("Insertion sort: ")
    print("------------------")
    if not array:
        print("Empty Array")
    if len(array) == 1:
        print(array)
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while j > 0 and array[j - 1] > key:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key
    pass
    print_array(array)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:  # If elements are out of order, swap them
                array[j], array[j + 1] = array[j + 1], array[i]
            pass
    pass
    print_array(array)


# Implementation of the selection sort algorithm
def selection_sort(array):
    #  checks if array is empty or already sorted (1 element)
    if not array:
        print("Empty Array")
    if len(array) == 1:
        print(array)
    else:
        # Traverse, i = sorted array
        for i in range(len(array)):
            min = array[i]  # Used to find minimum value
            swap = i
            # Find smallest value to swap
            for j in range(i + 1, len(array)):
                if array[j] < min:
                    min = array[j]
                    swap = j  # Index to be swapped

            # Swap values
            array[i], array[swap] = array[swap], array[i]

        print_array(array)
    pass


def heap_sort(array):
    if not array:
        print("Empty Array")
    if len(array) == 1:
        print(array)
    else:
        build_heap(array)
        length = len(array)
        for i in range((length-2)//2,-1,-1):
            pass
            heapify(array, i, length-1)

    pass

def build_heap(array):
    pass


def heapify(array,index,size):
    current = array[index]
    left = index*2
    right = index*2+1

    if(left <= len(array-1) )

    if()
    pass


def print_array(array):
    print(array)
    pass


def main():
    null_array = []
    single_array = [20]
    two_array = [20, 30]
    full_array = [20, 30, 10, 80, 60, 50, 40, 70]

    two_array_heap = [0, 20, 30]
    full_array_heap = [0, 20, 30, 10, 80, 60, 50, 40, 70]


    print("There are 6 available options to sort the arrays: ")
    print("")

    menu = {'1': "Insertion Sort",
            '2': "Selection Sort.",
            '3': "Bubble Sort",
            '4': "Merge Sort",
            '5': "Heap Sort",
            '6': "Quick Sort",
            '7': "Quit"}

    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])

        selection = str(input("Please make a selection:"))
        print(" ")

        if selection == '1':
            print("Insertion sort: ")
            print("------------------")
            insertion_sort(null_array)
            insertion_sort(single_array)
            insertion_sort(two_array)
            insertion_sort(full_array)
            print("")

        elif selection == '2':
            print("Selection sort: ")
            print("------------------")
            selection_sort(null_array)
            selection_sort(single_array)
            selection_sort(two_array)
            selection_sort(full_array)
            print("")

        elif selection == '3':
            print("Bubble sort: ")
            print("------------------")
            bubble_sort(null_array)
            bubble_sort(single_array)
            bubble_sort(two_array)
            bubble_sort(full_array)
            print("")

        elif selection == '4':
            print("Merge sort: ")
            print("------------------")
            merge_sort(null_array)
            merge_sort(single_array)
            merge_sort(two_array)
            merge_sort(full_array)
            print("")

        elif selection == '5':
            print("Heap sort: ")
            print("------------------")
            heap_sort(null_array)
            heap_sort(single_array)
            heap_sort(two_array)
            heap_sort(full_array)
            print("")

        elif selection == '6':
            print("Quick sort: ")
            print("------------------")
            quick_sort(null_array)
            quick_sort(single_array)
            quick_sort(two_array)
            quick_sort(full_array)
            print("")

        elif selection == '7':
            break
        else:
            print("Please choose 1, 2, 3, 4, 5, 6, or 7 to quit! ")
