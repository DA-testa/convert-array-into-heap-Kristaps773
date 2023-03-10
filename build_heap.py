#Krists Kristaps Dūda 221RDB518 10.grupa
# python3



def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        swaps += sift_down(data, i, n)
    return swaps


def sift_down(data, i, n):
    swaps = []
    while True:
        mini = i
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        if leftChild < n and data[leftChild] < data[mini]:
            mini = leftChild
        if rightChild < n and data[rightChild] < data[mini]:
            mini = rightChild
        if i != mini:
            data[i], data[mini] = data[mini], data[i]
            swaps.append((i, mini))
            i = mini
        else:
            break
    return swaps


def main():

    input1 = input()
    if 'F' in input1:
        file = input()
        file = "tests/" + file
        try:
            with open(file, mode = "r") as f:
                    n = int(f.readline())
                    data = list(map(int, f.readline().split()))
                    swaps = build_heap(data)
                    print(len(swaps))
                    for i, j in swaps:
                        print(i, j)
        except FileNotFoundError:
            return
        
    if 'I' in input1:
        n = int(input())
        data = list(map(int, input().split()))
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    else:
        return
    

    assert len(data) == n


if __name__ == "__main__":
    main()
