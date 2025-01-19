def get_digits(n):
    """Get list of digits in number n."""
    return [int(d) for d in str(n)]

def can_reach_one(n, memo=None):
    """Check if number n can reach 1 using the given operations."""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 1:
        return True
    
    digits = [d for d in get_digits(n) if d > 1]
    
    for digit in digits:
        if n % digit == 0:
            new_n = n // digit
            if can_reach_one(new_n, memo):
                memo[n] = True
                return True
    
    memo[n] = False
    return False

def solve(N):
    """Count valid numbers from 1 to N."""
    count = 0
    memo = {}
    
    if N >= 9:
        count = 9 

        for i in range(10, N + 1):
            if can_reach_one(i, memo):
                count += 1
    else:
        for i in range(1, N + 1):
            if can_reach_one(i, memo):
                count += 1
                
    return count

def main():
    N = int(input())
    print(solve(N))

if __name__ == "__main__":
    main()






################################### - Solution 2 - ####################################
def get_digits(n):
    """Get list of digits in number n."""
    return [int(d) for d in str(n)]

def can_reach_one(n, memo=None):
    """Check if number n can reach 1 using the given operations."""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 1:
        return True
    
    digits = [d for d in get_digits(n) if d > 1]
    
    for digit in digits:
        if n % digit == 0:
            new_n = n // digit
            if can_reach_one(new_n, memo):
                memo[n] = True
                return True
    
    memo[n] = False
    return False

def solve(N):
    """Count valid numbers from 1 to N."""
    count = 0
    memo = {} 
    if N >= 9:
        count = 9
        for i in range(10, N + 1):
            if can_reach_one(i, memo):
                count += 1
    else:
        for i in range(1, N + 1):
            if can_reach_one(i, memo):
                count += 1
                
    return count

def main():
    N = int(input())
    print(solve(N))

if __name__ == "__main__":
    main()