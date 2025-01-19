import sys

def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N = int(input())  # Number of points
        min_s = float('inf')
        max_s = float('-inf')

        for _ in range(N):
            x, y = map(int, input().split())  # Read x and y
            s = x + y  # Calculate s = x + y
            if s < min_s:
                min_s = s
            if s > max_s:
                max_s = s

        print(2 * (max_s - min_s))  # Output the result

if __name__ == "__main__":
    main()