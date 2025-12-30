def main():
    n = int(input())
    count = 0
    p = 5
    while p <= n:
        count += n // p
        p *= 5
    print(count)

if __name__ == "__main__":
    main()
