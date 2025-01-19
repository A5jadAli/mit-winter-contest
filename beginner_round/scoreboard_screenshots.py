def valid_ordering(N, K, screenshots):
    sorted_indices = sorted(range(N), key=lambda i: screenshots[i])
    for j in range(K): 
        for i in range(1, N): 
            if screenshots[sorted_indices[i - 1]][j] > screenshots[sorted_indices[i]][j]:
                print("NO")
                return

    print("YES")
    print(" ".join(map(str, [index + 1 for index in sorted_indices])))

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    N, K = map(int, data[:2])

    screenshots = []
    idx = 2
    for _ in range(N):
        screenshots.append(list(map(int, data[idx:idx + K])))
        idx += K
    valid_ordering(N, K, screenshots)