from collections import deque

def main():
    n: int = int(input())
    moves: list[tuple[int]] = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
    dist: list[list[int]] = [[-1] * n for _ in range(n)] 
    dist[0][0] = 0
    queue = deque()
    queue.append((0, 0))

    while queue:
        row, col = queue.popleft()
        for dr, dc in moves:
            next_row = row + dr
            next_col = col + dc
            if 0 <= next_row < n and 0 <= next_col < n and dist[next_row][next_col] == -1:
                dist[next_row][next_col] = dist[row][col] + 1
                queue.append((next_row, next_col))

    for cell in dist:
        print(*cell)


 

if __name__ == "__main__":
    main()
