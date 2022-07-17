# bubble-sort-python
def bubblesort(a):

    while True:

        put_flag = True

        for i in range(len(a) - 1):

            j = i + 1

            if a[i] > a[j]:

                put_flag = False

                temp = a[i]

                a[i] = a[j]

                a[j] = temp

        if put_flag:

            break

    return a
