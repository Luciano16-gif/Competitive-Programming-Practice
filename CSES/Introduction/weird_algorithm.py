def main() -> None: 
    while True:
        try: 
            n = int(input())
            if n <= 0 or n > (10**6):
                continue
            break
        except ValueError:
            continue

    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2       
        else:
            n = (n * 3) + 1
        seq.append(n)

    print(*seq)

if __name__ == "__main__":
    main()