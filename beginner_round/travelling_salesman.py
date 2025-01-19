def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve_tsp(n, cities):
    # Create distance matrix
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = manhattan_distance(cities[i][0], cities[i][1], 
                                         cities[j][0], cities[j][1])
    
    # dp[mask][pos] represents minimum distance to visit all cities in mask
    # ending at position pos
    dp = {}
    
    def tsp(mask, pos):
        if mask == (1 << n) - 1:  # All cities visited
            return dist[pos][0]  # Return to starting city
        
        state = (mask, pos)
        if state in dp:
            return dp[state]
        
        ans = float('inf')
        # Try visiting unvisited cities
        for city in range(n):
            if not (mask & (1 << city)):  # If city is not visited
                new_dist = dist[pos][city] + tsp(mask | (1 << city), city)
                ans = min(ans, new_dist)
        
        dp[state] = ans
        return ans
    
    # Start from city 1 (index 0), mark it as visited
    return tsp(1, 0)  # 1 represents binary 0001, city 1 visited

def main():
    t = int(input())  # Number of test cases
    
    for _ in range(t):
        n = int(input())  # Number of cities
        cities = []
        
        # Read coordinates for each city
        for _ in range(n):
            x, y = map(int, input().split())
            cities.append((x, y))
        
        # Solve and print result
        result = solve_tsp(n, cities)
        print(result)

if __name__ == "__main__":
    main()