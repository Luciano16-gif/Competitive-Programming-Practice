def main():
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if (row+col) % 2 == 0:
                if grid[row][col] == "A":
                    grid[row][col] = "B"
                else:
                    grid[row][col] = "A"
            else:
                if grid[row][col] == "C":
                    grid[row][col] = "D"
                else:
                    grid[row][col] = "C"

    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    main()