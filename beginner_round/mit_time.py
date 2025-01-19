def get_mit_time_classification(N):
    """
    Determine the MIT time classification for N minutes late.
    Returns the appropriate string format: "MIT time" or "MIT^k time"
    """
    if N <= 5:
        return "MIT time"
    
    # Find the appropriate power k where 5^(k-1) < N <= 5^k
    power = 2
    prev_limit = 5
    
    while True:
        current_limit = prev_limit * 5
        if prev_limit < N <= current_limit:
            return f"MIT^{power} time"
        power += 1
        prev_limit = current_limit
        
        # Safety check for large numbers
        if current_limit > 10**9:
            break

def solve():
    # Read number of test cases
    T = int(input())
    
    # Process each test case
    results = []
    for _ in range(T):
        N = int(input())
        result = get_mit_time_classification(N)
        results.append(result)
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()