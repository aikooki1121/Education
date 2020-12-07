my_list = []
print('Введите кол-во элементов массива и его элементы')
for a in range(0, int(input())):
    # t = int(input())
    my_list.append(int(input()))

my_list.sort()
print('my_list =', my_list, 'type: ', type(my_list))  # list check


def binary_search(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = round((low + high) / 2)
        # print('mid:', mid)
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid / 2
        return None


print('searched_element')
searched_element = int(input())
print(binary_search(my_list, searched_element))
