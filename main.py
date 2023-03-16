# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threadfin = [0] * n
    
    x = [None] * n
    
    for i in range(m):
        nextt = min(range(n), key=lambda x: threadfin[x])
        start = threadfin[nextt]
        threadfin[nextt] += data[i]
        output.append((nextt, start))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count    
    # TODO: print out the results, each pair in it's own line
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    
    for pair in result:
        print(pair[0], pair[1])
    




if __name__ == "__main__":
    main()
