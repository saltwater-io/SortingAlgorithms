# 6 Sorting Alogrithms
# Written by Dakota McGuire 3/1/19

# Code based on psuedocode and explanations by: https://www.youtube.com/watch?v=TzeBrDU-JaY
def merge_sort(array):
    # if not len(array):
    #     print("Empty Array")
    # elif len(array) == 1:
    #     print(array)
    # elif len(array) == 2:
    #     if array[0] > array[1]:
    #         array[0], array[1] = array[1], array[0]
    # else:
        if len(array) > 1:
            middle = len(array) // 2
            left = array[: middle]
            right = array[middle :]
            # Recursive call left side
            merge_sort(left)
            # Recursive call right side
            merge_sort(right)

            count_left = 0  # left array index
            count_right = 0  # Right array index
            count_merge = 0  # Merged array index

            while count_left < len(left) and count_right < len(right):
                # Is left element < right element? If so, then move left element into array and increment the count
                if left[count_left] < right[count_right]:
                    array[count_merge] = left[count_left]
                    count_left = count_left + 1
                # Is the right element < left element? If so move right element into array and index the count
                elif left[count_left] > right[count_right]:
                    array[count_merge] = right[count_right]
                    count_right = count_right + 1
                count_merge = count_merge + 1

            # If anymore elements on left side, add them to to array
            while count_left < len(left):
                array[count_merge] = left[count_left]
                count_merge = count_merge + 1
                count_left = count_left + 1
            # If anymore elements on left side, add them to array
            while count_right < len(right):
                array[count_merge] = right[count_right]
                count_merge = count_merge + 1
                count_right = count_right + 1
        # print(temp_array)
        pass

# Code based on psuedocode found here: https://users.cs.duke.edu/~reif/courses/alglectures/skiena.lectures/lecture5.pdf
def quick_sort(array, low, high):
    # if not len(array):
    #     print("Empty Array")
    # elif len(array) == 1:
    #     print(array)
    # elif len(array) == 2:
    #     if array[0] > array[1]:
    #         array[0], array[1] = array[1], array[0]
    # else:

    #     If lower bounds lower, or not the same index as the higher bounds
    if low < high:
        # Get a partiton index
        partition_index = partition(array, low, high)
        # Recursively sort right and left sides.
        quick_sort(array, partition_index + 1, high)
        quick_sort(array, low, partition_index - 1)


# Code based on psuedocode found here: https://users.cs.duke.edu/~reif/courses/alglectures/skiena.lectures/lecture5.pdf
def partition(array, low_bound, high_bound):
        # Pivot
        pivot = array[high_bound]
        # Lower Index
        index = low_bound - 1
        # for each number inside range, if its lower than the pivot it increments the index and swaps the values
        for i in range(low_bound, high_bound):
            if array[i] < pivot:
                index += 1
                array[index], array[i] = array[i], array[index]
        # Moves pivot to index + 1 and returns it
        array[index + 1], array[high_bound] = array[high_bound], array[index + 1]
        return index + 1


# Code based on pseudocode found in slides
def insertion_sort(array):
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


# Implementation of the bubble sort algorithm
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
        for i in range((length - 2) // 2, -1, -1):
            pass
            heapify(array, i, length - 1)

    pass


def build_heap(array):
    pass


def heapify(array, index, size):
    pass
    # current = array[index]
    # left = index*2
    # right = index*2+1
    #
    # if(left <= len(array-1) )
    #
    # if()
    # pass


def print_array(array):
    print(array)
    pass


def main():

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

        # Arrays to be tested
        null_array = []
        single_array = [20]
        two_array = [20, 30]
        full_array = [20, 30, 10, 80, 60, 50, 40, 70]

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
            print_array(null_array)
            print_array(single_array)
            print_array(two_array)
            print_array(full_array)

            print("")

        elif selection == '5':
            print("Heap sort: ")
            print("------------------")
            heap_sort(null_array)
            heap_sort(single_array)
            heap_sort(two_array)
            heap_sort(full_array)
            print_array(null_array)
            print_array(single_array)
            print_array(two_array)
            print_array(full_array)
            print("")

        elif selection == '6':
            print("Quick sort: ")
            print("------------------")
            quick_sort(null_array, 0, len(null_array))
            quick_sort(single_array, 0, len(single_array)-1)
            quick_sort(two_array, 0, len(two_array) - 1)
            quick_sort(full_array, 0, len(full_array) - 1)
            print_array(null_array)
            print_array(single_array)
            print_array(two_array)
            print_array(full_array)
            print("")

        elif selection == '7':
            break
        else:
            print("Please choose 1, 2, 3, 4, 5, 6, or 7 to quit! ")


if __name__ == "__main__":
    main()

