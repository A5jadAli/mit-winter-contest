def is_repetitive(s):
    """Check if string is M + multiple ITs"""
    if len(s) < 3 or s[0] != 'M':
        return False
    
    s = s[1:]  # Remove the M
    if len(s) % 2 != 0:  # Rest should be pairs of IT
        return False
        
    # Check each pair is IT
    return all(s[i:i+2] == "IT" for i in range(0, len(s), 2))

def check_string(s):
    """Check if string can be split into repetitive strings"""
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is valid
    
    # For each position in string
    for i in range(1, n + 1):
        # Try all possible strings ending at position i
        for j in range(i):
            if dp[j] and is_repetitive(s[j:i]):
                dp[i] = True
                break
    
    return dp[n]

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input().strip()
        print("YES" if check_string(s) else "NO")

if __name__ == "__main__":
    main()