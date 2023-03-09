#Krists Kristaps Dūda 221RDB518 10.grupa
# python3


def main():

    ##TO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input1 = input("Enter 'i' to input from keyboard, 'f' to input from file: ")
    if input1.lower() == 'f':
        filename = input("File path: ")
        with open(f'{filename}') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
    elif input1.lower() == 'i':
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
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

def build_heap(data):
    swaps = []
    # TO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n//2,-1,-1):
        j=i
        while True:
            mini = j
            leftChild = 2*j + 1
            rightChild = 2*j + 2
            if leftChild < n and data[leftChild] < data[mini] :
                mini = leftChild
            if rightChild < n and data[rightChild] < data[mini] :
                mini = rightChild
            if j!=mini:
                data[j], data[mini] = data[mini], data[j]
                swaps.append((j, mini))
                j = mini
            else:
                break

    return swaps

