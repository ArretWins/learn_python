import numpy as np


def main():
    # a = np.arange(8)
    # print(a)
    # print(type(a))
    # b = np.array([1, 2, 3], dtype=np.int8)
    # #print(type(b[0]))
    # b = np.array([[1, 2, 3],[4, 5, 6]], dtype=np.int8)

    # eye_array = np.eye(7, k=1,dtype=np.int8)
    # eye_array[eye_array == 0] = 2
    # eye_array[5] = 8
    # eye_array[:2] = 3
    # eye_array[6:] = 1
    # eye_array[:, -1] = 0
    # print(eye_array)

    a = np.zeros((3, 3), dtype=np.int8)
    a.fill(7)
    a[:2] = 2
    print('Array A\n', a)

    array_sum = a.sum()
    #print('Sum \n', array_sum)

    b = np.arange(1, 10, dtype=np.int8).reshape(3, 3)

    print('Array B\n', b)

    #flatten arrays
    array_flat = b.reshape(b.size)
    array_flat = b.flatten()
    array_flat = b.ravel()
    #print(array_flat)

    #repeat values/arrays
    array_repeat = np.repeat(b, 3, axis=0)
    #print(array_repeat)

    #conversion and storage
    my_list = b.tolist()
    #print('b is', type(b))
    #print('my list is', type(my_list))
    #print('my list is\n', my_list)
    b.tofile('my_array.txt', sep = ',')

    #transposition
    array_swapped = np.swapaxes(b, 0, 1)
    array_swapped = b.transpose(1, 0 )
    array_swapped = b.T
    #print(array_swapped)

    #operations on 2 matrices
    simple_ops = a + b;
    print(simple_ops)

if __name__ == '__main__':
    main()
