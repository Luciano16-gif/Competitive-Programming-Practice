def main() -> None:
    board = [input().strip() for _ in range(8)]
    cols: list[bool] = [False] * 8
    diagonal1: list[bool] = [False] * 15
    diagonal2: list[bool] = [False] * 15
    ans: int = 0

    def mark_dismark(row, col, val) -> None:
        cols[col] = val
        diagonal1[row - col + 7] = val
        diagonal2[row + col] = val

    def dfs(row):
        nonlocal ans
        if row == 8:
            ans += 1
            return

        for col in range(8):
            if board[row][col] != "*" and not cols[col] and not diagonal1[row - col + 7] and not diagonal2[row + col]:
                mark_dismark(row, col, True)
                dfs(row+1)
                mark_dismark(row, col, False)

    dfs(0)
    print(ans)
        

if __name__ == "__main__":
    main()