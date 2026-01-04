def main() -> None:
    n = int(input())
    p: list[int] = list(map(int, input().split()))
    total: int = sum(p)
    best: int = total
    for i in range(1<<n):
        s: int = 0
        for j in range(n):
            if (i >> j) & 1:
                s += p[j]

        best = min(best, abs(total - 2*s))

    print(best)
            

if __name__ == "__main__":
    main()