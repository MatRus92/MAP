def ShellSort(myList):
    distance = len(myList) // 2
    while distance > 0:
        for i in range(distance, len(myList)):
            print(myList[distance: len(myList)])
            temp = myList[i]
            j = i
            while j >= distance and myList[j - distance] > temp:
                myList[j] = myList[j - distance]
                j = j - distance

            myList[j] = temp

        distance = distance // 2

    return myList


if __name__ == "__main__":
    print(ShellSort([232, 1, 4, 68, 11, 90, 43, 2, 54, 12, 0, 2422, 5, 21, 78, 65]))