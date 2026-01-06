def main() -> None:
    n:int = int(input())
    for i in range(n):
        row: list = []
        for j in range(n):
            row.append(i ^ j)
        print(*row)


if __name__ == "__main__":
    main()