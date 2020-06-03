
array_1 = ['hello', 'hello', 'hello', 2, 3, 3, 4, 5, 5]


def array(array_1):
    array_2 = []
    for item in array_1:
        if array_2.count(item) < 1:
            array_2.append(item)

    return array_2


print(array(array_1))















