 #Krists Kristaps Dūda 221RDB518 10.grupa
# python3



def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        j = i
        while True:
            tightChild = j * 2 + 2
            leftChild = j * 2 + 1
            mini = j
            if tightChild < n and data[tightChild] < data[mini]:
                mini = tightChild
            if leftChild < n and data[leftChild] < data[mini]:
                mini = leftChild
            if mini != j:
                swaps.append((j, mini))
                data[j], data[mini] = data[mini], data[j]
                j = mini
            else:
                break
    return swaps


def main():

    input1 = input()
    if 'F' in input1:
        file = input()
        file = "tests/" + file
        try:
            with open(file, mode="r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
                assert len(data) == n
        except FileNotFoundError:
            return
        
    if 'I' in input1:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    else:
        return
    

    # checks if lenght of data is the same as the said lenght
    #assert len(data) == n
    
    # calls function to assess the data,
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
