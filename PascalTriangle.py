from typing import List


def get_pascal(k: int) -> List[int]:
    row = [1 for _ in range(k)]
    print(row)
    curr = 1
    for _ in range(k):
        last = 0
        for i in range(curr - 1):
            last, temp = row[i], last
            print(last)
            print(temp)
            row[i] += temp
        curr += 1
    return row


if __name__ == "__main__":
    print(get_pascal(6))

