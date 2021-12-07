def countSort(arr):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(256)]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    return output


if __name__ == '__main__':
    arr = "MateuszRus1992Programowaniezpasja"
    ans = countSort(arr)
    print(" Lista posortowanych znaków w tablicy % s" % ("".join(ans)))



