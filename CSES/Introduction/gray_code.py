def main() -> None:
    n: int = int(input())
    for i in range(1 << n):
        g = i ^ (i >> 1)
        print(f"{g:0{n}b}")


if __name__ == "__main__":
    main()