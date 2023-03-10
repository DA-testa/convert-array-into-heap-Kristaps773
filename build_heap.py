 #Krists Kristaps Dūda 221RDB518 10.grupa
# python3



def build_heap(data):
    swaps = []
    # TO: Create heap and heap sort
    # try to achieve O(n) and not O(n^2)
    size = len(data)
    for parent in range(size // 2, -1, -1):
        while 2 * parent + 1 < size:
            leftChild = 2 * parent + 1
            rightChild = leftChild + 1 if leftChild + 1 < size and data[leftChild + 1] < data[leftChild] else leftChild
            if data[parent] <= data[rightChild]:
                break
            swaps.append((parent, rightChild))
            data[parent], data[rightChild] = data[rightChild], data[parent]
    return swaps



def main():

    ##TO : add input and corresponding checks
    # add another input for leftChildor F 
    # first two tests are from keyboard, third test is from a file
    input1 = input()
    if 'F' in input1:
        file = input()
        file = "test/" + file
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
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    
    # calls function to assess the data,
    # and give back all swaps
    #swaps = build_heap(data)

    ##T: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    #print(len(swaps))
    #for i, j in swaps:
    #    print(i, j)


if __name__ == "__main__":
    main()
