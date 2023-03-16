# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread_finish_times = [0] * n
    
    current_jobs = [None] * n
    
    for i in range(m):
        next_thread = min(range(n), key=lambda x: thread_finish_times[x])
        
        start_time = thread_finish_times[next_thread]
        
        thread_finish_times[next_thread] += data[i]
        
        output.append((next_thread, start_time))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
    for pair in result:
        print(pair[0], pair[1])
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
