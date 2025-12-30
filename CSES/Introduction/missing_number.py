def main() -> None:
    n = int(input())
    nums: set[int] = set(map(int, input().split()))

    for i in range(1, n + 1):
        if i not in nums:
            print(i)
            break


if __name__ == "__main__":
    main()