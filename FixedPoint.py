from typing import List


def fixed_point(arr: List[int]):
    for index, value in enumerate(arr):
        if value == index:
            return value
        else:
            continue
    return False


if __name__ == "__main__":
    print(fixed_point([1, 5, 7, 8]))
    print(fixed_point([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]))
    print(fixed_point([-6, 0, 40, 3]))

