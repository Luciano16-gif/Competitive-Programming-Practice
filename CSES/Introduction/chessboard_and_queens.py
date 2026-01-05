def main() -> None:
    board = [input().strip() for _ in range(8)]
    col: list[bool] = [False] * 8
    diag1: list[bool] = [False] * 15
    diag2: list[bool] = [False] * 15
    ans: int = 0

    def mark_dismark(r, c, val) -> None:
        col[c] = val
        diag1[r - c + 7] = val
        diag2[r + c] = val

    def dfs(r):
        nonlocal ans
        if r == 8:
            ans += 1
            return

        for c in range(8):
            if board[r][c] != "*" and not col[c] and not diag1[r - c + 7] and not diag2[r + c]:
                mark_dismark(r, c, True)
                dfs(r+1)
                mark_dismark(r, c, False)

    dfs(0)
    print(ans)
        

if __name__ == "__main__":
    main()