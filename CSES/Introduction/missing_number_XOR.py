def main() -> None:
    n = int(input())
    nums: list[int] = list(map(int, input().split()))

    x = 0
    for i in range(1, n+1):
        x ^= i
    
    for i in nums:
        x ^= i

    print(x)



if __name__ == "__main__":
    main()