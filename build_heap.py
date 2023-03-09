#Krists Kristaps Dūda 221RDB518 10.grupa
# python3




def build_heap(data):
    swaps = []
    # TO: Create heap and heap sort
    # try to achieve O(n) and not O(n^2)
    n = len(data)
    for i in range(n // 2, -1, -1):
        j = i
        while True:
            mini = j
            left_child = 2 * j + 1
            right_child = 2 * j + 2
            if left_child < n and data[left_child] < data[mini]:
                mini = left_child
            if right_child < n and data[right_child] < data[mini]:
                mini = right_child
            if j != mini:
                data[j], data[mini] = data[mini], data[j]
                swaps.append((j, mini))
                j = mini
            else:
                break

    return swaps


def main():
    ##TO: add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file
    input1 = input("Enter 'i' to input from keyboard, 'f' to input from file: ")
    data = []
    if input1.lower() == 'f':
        filename = input("File path: ")
        with open(f'{filename}') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    elif input1.lower() == 'i':
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    ##T: output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
