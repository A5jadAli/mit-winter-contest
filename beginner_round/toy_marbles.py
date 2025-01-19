def organize_marbles(n, marbles):
    actions = []
    visited = [False] * (n + 1)
    position_map = {}

    # Store the positions in position_map
    for i in range(n):
        position_map[marbles[i]] = i + 1

    for i in range(1, n + 1):
        if visited[i] or marbles[i - 1] == i:
            continue

        cycle = []
        current = i

        # Detect the cycle for the current element
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = position_map[current]

        # Record the operations for this cycle
        for j in range(len(cycle) - 1):
            actions.append(f"1 {cycle[j]} {cycle[j + 1]}")

    # Output the result
    print(len(actions))
    for action in actions:
        print(action)

def main():
    n = int(input())  # Read the size of the array
    marbles = list(map(int, input().split()))  # Read the marbles positions

    organize_marbles(n, marbles)

if __name__ == "__main__":
    main()