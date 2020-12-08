arr = []
print('Введите кол-во элементов массива и его элементы')
for a in range(0, int(input())):
    # t = int(input())
    arr.append(int(input()))

# my_list.sort()
print('my_list =', arr, 'type: ', type(arr))  # list check


def findSmaller(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmaller(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print('smaller_index:', findSmaller(arr))
print('sorted list:', selectionSort(arr))

# arr = [5, 3, 6, 2, 10]5
# print(range(1, len(arr)))
