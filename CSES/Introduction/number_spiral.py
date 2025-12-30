def main() -> None:
    results = []
    t = int(input())
    for _ in range(t):
        y, x = map(int, input().split())
        if y >= x:
            if y % 2 == 0:
                results.append(y**2 - (x-1))
            else:
                results.append(((y-1)**2 + 1) + (x-1)) 
        else:
            if x % 2 == 0:
                results.append(((x-1)**2 + 1) + (y-1))
            else:
                results.append(x**2 - (y-1))

    for x in results:
        print(x)


if __name__ == "__main__":
    main()